import dns.resolver
import dns.exception

def query_dns_records(domain, record_type):
    try:
        answers = dns.resolver.resolve(domain, record_type)
        for rdata in answers:
            print(f"{record_type} Record: {rdata.to_text()}")
    except dns.exception.DNSException as e:
        print(f"No {record_type} record found for {domain} or error occurred: {e}")


def main(domain):

    # Query various DNS record types
    record_types = ['A', 'AAAA', 'CNAME', 'MX', 'NS', 'PTR', 'TXT', 'SRV', 'SOA', 'CAA']
    for record_type in record_types:
        query_dns_records(domain, record_type)


if __name__ == '__main__':
    domain_name = input('Domain name to search: ')
    main(domain=domain_name)
