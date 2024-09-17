import logging
import grpc

import unter_pb2 as pb
import unter_pb2_grpc as rpc



logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%dT%H:%M:%S',
)

class Unter(rpc.UnterServicer):
    def StartRide(self, request: pb.StartRideRequest, context: grpc.ServicerContext):
        logging.info('start: id=%s', request.id)
        resp = pb.StartRideResponse(
            id=request.id,
        )
        return resp

if __name__ == '__main__':
    from concurrent.futures import ThreadPoolExecutor

    from grpc_reflection.v1alpha import reflection


    server = grpc.server(
        thread_pool=ThreadPoolExecutor(),
    )

    unter = Unter()
    rpc.add_UnterServicer_to_server(unter, server)
    services = (
        pb.DESCRIPTOR.services_by_name['Unter'].full_name,
        reflection.SERVICE_NAME,
    )
    reflection.enable_server_reflection(services, server)

    port = 9876
    server.add_insecure_port(f'[::]:{port}')
    server.start()
    logging.info('server running on port %d', port)
    server.wait_for_termination()
