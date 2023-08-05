import ifaddr


def get_addresses() -> list[ifaddr.IP]:
    return [addr for iface in ifaddr.get_adapters() for addr in iface.ips]


def get_ips() -> list[str]:
    [addr.ip if addr.is_IPv4 else addr.ip[0] for addr in get_addresses()]