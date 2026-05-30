param([string]$url, [string]$out)

function Get-PageWithRedirect([string]$url) {
    try {
        $resp = Invoke-WebRequest -Uri $url -UserAgent "Mozilla/5.0" -TimeoutSec 25 -UseBasicParsing
        return $resp.Content
    } catch {
        $locHeader = $_.Exception.Response.Headers["Location"]
        if ($locHeader) {
            $loc = $locHeader[0]
            if ($loc -notmatch "^https?://") { $loc = "https://www.leantalk.cn" + $loc }
            return Get-PageWithRedirect $loc
        }
        throw
    }
}

$html = Get-PageWithRedirect $url
$html | Out-File -FilePath $out -Encoding utf8
Write-Host "DONE: $url -> $out"