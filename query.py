import dns.resolver 


class DNS_Whisperer:
    """DNS Enumeration tool"""

    def __init__(self, domain, record): 
        self.domain = domain
        self.record = record
    def lookup(self): 
        try:
            responses = dns.resolver.resolve(self.domain, self.record) 
            for response in responses: # Dumps DNS records
                print(response)       
        except dns.resolver.NXDOMAIN: 
            print("This domain does not exist")
        except dns.resolver.NoAnswer:
            print(f"Unable to find {self.record} record")
        except dns.resolver.Timeout:
            print("DNS Request timed out")
