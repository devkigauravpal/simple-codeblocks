Start-Transcript -Path "log_trace.txt"
Import-Csv urls.csv |
ForEach-Object {
Write-Host "Testing : " $_.url "'r"

}
Stop-Transcript