from aternos import Aternos

at = Aternos("wbananasmp", "wbananasmp")
servers = at.list_servers()
server = servers[0]
server.start()
print("✅ Server started!")
