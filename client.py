import unter_pb2 as pb
import unter_pb2_grpc as rpc
import grpc

def start():
    req = pb.StartRideRequest(
        id='red5',
        kind=pb.KIND_SHARED,
        driver_id='C3-PO',
    )
    req.time.GetCurrentTime()

    with grpc.insecure_channel('localhost:9876') as ch:
        client = rpc.UnterStub(ch)
        try:
            # resp = client.StartRide(req)
            resp = client.StartRide(
                req,
                metadata=(
                    ('token', 'C-3PO'),
                ),
            )
        except grpc.RpcError as err:
            code = err.code().name
            details = err.details()
            print(f'error: {details} ({code})')

            # state = err.args[0]
            # print(state.target, state.method)
            # print(err.code())
            # breakpoint()
            return

        print(resp.id)


if __name__ == '__main__':
    start()
