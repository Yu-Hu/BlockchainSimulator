from servers import server


class UDPRouter(server.UDPRequestHandler):
    """
    The UDP router for handling requests from nodes in the peer to peer network and passing them
    to the router to be routed to the node's corresponding handler.
    """

    def __init__(self, request, client_address, serv):
        server.UDPRequestHandler.__init__(self, request, client_address, serv)

    def receive(self, data):
        """
        Received binary messages from other nodes in the peer to peer network.
        :param data: The binary data which should be decodable using the Request protocol buffer.
        :return: None
        """
        self.server.router.route(data, self)
