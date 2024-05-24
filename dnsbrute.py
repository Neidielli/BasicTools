import dns.resolver

# Create a DNS resolver instance
res = dns.resolver.Resolver()

# Open the wordlist file containing common subdomains
# Replace "/home/kali/wordlist.txt" with the path to your wordlist file
arquiv = open("/home/kali/wordlist.txt", "r")

# Read the contents of the wordlist and split it into lines
subdomains = arquiv.read().splitlines()

target = "localhost"

# Iterate through each subdomain in the wordlist
for subdomain in subdomains:
	try:
		sub_target = subdomain + "." + target
		# Resolve the subdomain to an IP address (A record) 
		result = res.resolve(sub_target, "A")
		for ip in result:
			print(sub_target, "->", ip)
	except:
		pass
