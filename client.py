import unter_pb2 as pb
import unter_pb2_grpc as rpc
import grpc
from time import sleep

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
            return

        print(resp.id)


def iter_locs():
    lat, lng = 28.5244425,-16.38491
    for _ in range(5):
        lat -= 0.0001
        lng += 0.0001
        loc = pb.Location(
            ride_id='red5',
            lat=lat,
            lng=lng,
        )
        yield loc
        sleep(0.7)  # Simulate work


def track():
    with grpc.insecure_channel('localhost:9876') as ch:
        client = rpc.UnterStub(ch)
        resp = client.Track(iter_locs())
        print(resp)



if __name__ == '__main__':
    start()
    track()
