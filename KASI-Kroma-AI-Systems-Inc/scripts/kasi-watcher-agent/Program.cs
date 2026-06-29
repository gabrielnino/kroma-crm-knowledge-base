using System;
using System.IO;
using System.Text;
using System.Text.RegularExpressions;
using System.Diagnostics;
using System.Threading;

namespace KasiWatcherAgent
{
    class Program
    {
        private static readonly string TargetPath = @"F:\kroma-crm-knowledge-base\KASI-Kroma-AI-Systems-Inc\";
        private static readonly string IndexerScript = Path.Combine(TargetPath, "scripts", "indexer.py");

        static void Main(string[] args)
        {
            Console.WriteLine("============================================================");
            Console.WriteLine(" KASI CRM - Agente FileSystemWatcher Inicializado");
            Console.WriteLine($" Monitoreando: {TargetPath}");
            Console.WriteLine(" Presiona Enter para detener el agente.");
            Console.WriteLine("============================================================");

            using (FileSystemWatcher watcher = new FileSystemWatcher())
            {
                watcher.Path = TargetPath;
                watcher.IncludeSubdirectories = true;
                watcher.NotifyFilter = NotifyFilters.FileName | NotifyFilters.LastWrite;
                
                // Filtramos archivos creados y renombrados
                watcher.Created += OnFileEvent;
                watcher.Renamed += OnFileRenamed;

                watcher.EnableRaisingEvents = true;

                Console.ReadLine();
            }
        }

        private static void OnFileRenamed(object sender, RenamedEventArgs e)
        {
            ProcessFile(e.FullPath);
        }

        private static void OnFileEvent(object sender, FileSystemEventArgs e)
        {
            ProcessFile(e.FullPath);
        }

        private static void ProcessFile(string filePath)
        {
            try
            {
                // 1. Validaciones básicas y exclusiones para evitar bucles infinitos
                if (!File.Exists(filePath)) return;

                string extension = Path.GetExtension(filePath).ToLower();
                string fileName = Path.GetFileName(filePath);
                string directory = Path.GetDirectoryName(filePath) ?? "";

                // Ignorar archivos del sistema, Git, carpetas de scripts o recursos
                if (directory.Contains(@"\.git") || 
                    directory.Contains(@"\.gemini") || 
                    directory.Contains(@"\scripts") || 
                    directory.Contains(@"\recursos") ||
                    fileName.Equals("change-log.md", StringComparison.OrdinalIgnoreCase) ||
                    fileName.StartsWith(".") ||
                    extension == ".tmp" ||
                    extension == ".db" ||
                    extension == ".log")
                {
                    return;
                }

                Console.WriteLine($"\n[DETECTADO]: {fileName} en {directory}");

                // Esperar a que el archivo deje de estar bloqueado por el proceso de escritura
                if (!WaitForFile(filePath))
                {
                    Console.WriteLine($"[ADVERTENCIA]: No se pudo obtener acceso exclusivo al archivo {fileName}. Omitiendo procesamiento.");
                    return;
                }

                // Identificar si pertenece a un cliente
                string clientFolder = GetClientFolder(filePath);
                if (string.IsNullOrEmpty(clientFolder))
                {
                    Console.WriteLine("[INFO]: El archivo no pertenece a la carpeta de un cliente. Omitiendo reubicación.");
                    return;
                }

                // 2. NOMENCLATURE ANALYSIS & ALIGNMENT (Normalizar nombre)
                string nameWithoutExt = Path.GetFileNameWithoutExtension(filePath);
                string normalizedNameWithoutExt = NormalizeName(nameWithoutExt);
                string targetFileName = normalizedNameWithoutExt + extension;
                
                // 3. DIRECTORY VERIFICATION & PLACEMENT (Ubicación lógica)
                string targetSubFolder = GetTargetSubFolder(extension, fileName, filePath);
                string clientPath = Path.Combine(TargetPath, "Custumers", clientFolder);
                string targetDirectory = Path.Combine(clientPath, targetSubFolder);

                // Crear subcarpeta de destino si no existe
                if (!Directory.Exists(targetDirectory))
                {
                    Directory.CreateDirectory(targetDirectory);
                }

                string finalDestinationPath = Path.Combine(targetDirectory, targetFileName);

                // Si ya está en la ubicación correcta y con el nombre correcto, no hacemos nada para evitar bucles
                if (string.Equals(filePath, finalDestinationPath, StringComparison.OrdinalIgnoreCase))
                {
                    return;
                }

                Console.WriteLine($"[PASO 2 & 3]: Organizando archivo...");
                Console.WriteLine($"  Origen: {filePath}");
                Console.WriteLine($"  Destino: {finalDestinationPath}");

                // Mover / renombrar archivo
                if (File.Exists(finalDestinationPath))
                {
                    // Si ya existe un archivo con ese nombre, agregamos un timestamp
                    string timestamp = DateTime.Now.ToString("yyyyMMddHHmmss");
                    finalDestinationPath = Path.Combine(targetDirectory, $"{normalizedNameWithoutExt}-{timestamp}{extension}");
                }
                
                File.Move(filePath, finalDestinationPath);

                // 4. INDEXATION UPDATE (Re-indexar base de datos de conocimiento)
                Console.WriteLine("[PASO 4]: Ejecutando re-indexación de la base de conocimiento...");
                RunIndexer();

                // 5. CHANGELOG REGISTRATION (Registrar en el changelog del cliente)
                Console.WriteLine("[PASO 5]: Registrando evento en el changelog del cliente...");
                RegisterInChangelog(clientPath, clientFolder, Path.GetFileName(finalDestinationPath), targetSubFolder);

                Console.WriteLine("[COMPLETADO]: Ciclo de mantenimiento finalizado de forma exitosa.");
            }
            catch (Exception ex)
            {
                Console.WriteLine($"[ERROR]: Ocurrió una falla durante el procesamiento del archivo: {ex.Message}");
            }
        }

        private static string NormalizeName(string name)
        {
            // Convertir a minúsculas
            string result = name.ToLower();
            
            // Reemplazar espacios y guiones bajos por guiones medios
            result = result.Replace(" ", "-").Replace("_", "-");
            
            // Remover caracteres especiales no deseados (manteniendo guiones y alfanuméricos)
            result = Regex.Replace(result, @"[^a-z0-9\-]", "");
            
            // Remover guiones múltiples seguidos (ej. --- o --)
            result = Regex.Replace(result, @"\-+", "-");
            
            // Limpiar guiones en extremos
            return result.Trim('-');
        }

        private static string GetClientFolder(string filePath)
        {
            // Buscamos la carpeta del cliente en la ruta: TargetPath\Custumers\<ClientName>\...
            string relativePath = Path.GetRelativePath(TargetPath, filePath);
            string[] parts = relativePath.Split(Path.DirectorySeparatorChar);
            if (parts.Length > 2 && parts[0].Equals("Custumers", StringComparison.OrdinalIgnoreCase))
            {
                return parts[1]; // Nombre de la carpeta del cliente
            }
            return string.Empty;
        }

        private static string GetTargetSubFolder(string extension, string fileName, string filePath)
        {
            // Determinar carpeta correcta según extensión e indicios de contenido
            switch (extension)
            {
                case ".mp4":
                case ".mov":
                case ".avi":
                case ".mkv":
                    return "Videos";
                
                case ".txt":
                    // Si el nombre contiene palabras clave de chats o llamadas, va a Conversaciones
                    if (fileName.Contains("conversacion") || 
                        fileName.Contains("chat") || 
                        fileName.Contains("sms") || 
                        fileName.Contains("whatsapp") || 
                        fileName.Contains("minuta") || 
                        fileName.Contains("transcripcion") ||
                        fileName.Contains("call") ||
                        fileName.Contains("audio"))
                    {
                        return "Conversaciones";
                    }
                    return "Documentos";

                case ".json":
                case ".csv":
                case ".pdf":
                case ".docx":
                case ".xlsx":
                case ".doc":
                case ".xls":
                case ".ppt":
                case ".pptx":
                default:
                    return "Documentos";
            }
        }

        private static bool WaitForFile(string filePath)
        {
            // Intentar abrir el archivo de forma exclusiva para garantizar que terminó de escribirse
            int numTries = 0;
            while (numTries < 20)
            {
                try
                {
                    using (FileStream fs = new FileStream(filePath, FileMode.Open, FileAccess.ReadWrite, FileShare.None))
                    {
                        return true;
                    }
                }
                catch (IOException)
                {
                    numTries++;
                    Thread.Sleep(500); // Esperar 500ms antes de reintentar
                }
            }
            return false;
        }

        private static void RunIndexer()
        {
            try
            {
                ProcessStartInfo psi = new ProcessStartInfo
                {
                    FileName = "python",
                    Arguments = $"\"{IndexerScript}\" index",
                    RedirectStandardOutput = true,
                    RedirectStandardError = true,
                    UseShellExecute = false,
                    CreateNoWindow = true
                };

                using (Process process = Process.Start(psi)!)
                {
                    string output = process.StandardOutput.ReadToEnd();
                    string error = process.StandardError.ReadToEnd();
                    process.WaitForExit();

                    if (process.ExitCode == 0)
                    {
                        Console.WriteLine($"  [INDEXER OK]: {output.Trim()}");
                    }
                    else
                    {
                        Console.WriteLine($"  [INDEXER ERROR CODE {process.ExitCode}]: {error.Trim()}");
                    }
                }
            }
            catch (Exception ex)
            {
                Console.WriteLine($"  [INDEXER EXCEPTION]: {ex.Message}");
            }
        }

        private static void RegisterInChangelog(string clientPath, string clientFolder, string fileName, string subFolder)
        {
            try
            {
                string changelogPath = Path.Combine(clientPath, "change-log.md");
                string todayStr = DateTime.Now.ToString("yyyy-MM-dd");

                StringBuilder sb = new StringBuilder();
                if (!File.Exists(changelogPath))
                {
                    sb.AppendLine($"# CHANGELOG: {clientFolder.ToUpper()}");
                    sb.AppendLine("Registro de control de cambios y mutaciones documentales de la cuenta.");
                    sb.AppendLine();
                }
                else
                {
                    sb.Append(File.ReadAllText(changelogPath, Encoding.UTF8));
                }

                // Generar la entrada del log
                string entryBlock = $"- Carpeta `{subFolder}/` conteniendo el archivo `{fileName}` procesado y normalizado de forma automática.";
                
                string content = sb.ToString();
                string dateHeader = $"## [{todayStr}]";

                if (content.Contains(dateHeader))
                {
                    // Si ya existe la cabecera del día, inyectamos bajo la sección ### Agregado o directamente debajo del encabezado
                    int headerIndex = content.IndexOf(dateHeader);
                    int insertIndex = content.IndexOf("\n", headerIndex) + 1;
                    
                    // Buscar si tiene sección "### Agregado"
                    int agregadoIndex = content.IndexOf("### Agregado", headerIndex);
                    if (agregadoIndex != -1 && agregadoIndex < content.IndexOf("## [", headerIndex + 10) || (agregadoIndex != -1 && !content.Contains("## [", StringComparison.OrdinalIgnoreCase)))
                    {
                        insertIndex = content.IndexOf("\n", agregadoIndex) + 1;
                    }
                    
                    content = content.Insert(insertIndex, entryBlock + "\n");
                }
                else
                {
                    // Si no existe la fecha, agregamos la fecha y la entrada al final del documento
                    StringBuilder newDayBlock = new StringBuilder();
                    newDayBlock.AppendLine();
                    newDayBlock.AppendLine(dateHeader);
                    newDayBlock.AppendLine("### Agregado");
                    newDayBlock.AppendLine(entryBlock);
                    
                    content += newDayBlock.ToString();
                }

                File.WriteAllText(changelogPath, content, Encoding.UTF8);
                Console.WriteLine($"  [CHANGELOG OK]: Entrada registrada en {changelogPath}");
            }
            catch (Exception ex)
            {
                Console.WriteLine($"  [CHANGELOG ERROR]: No se pudo escribir en el changelog: {ex.Message}");
            }
        }
    }
}
