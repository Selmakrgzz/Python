import sys
import argparse

def valid_server(port_number):
    port = int(port_number)

    if 1025 <= port <= 65535:
        return port
    else:
        return argparse.ArgumentTypeError(f'Invalid port number: {port}')

def main():
    parser = argparse.ArgumentParser(description='Port address check')

    parser.add_argument('-s', '--server', dest='server', help='Specify server address')
    parser.add_argument('-p', '--port', dest='port', type=valid_server, help='Specify port number between 1025-65535')
    args=parser.parse_args()

    if args.server:
        print(f'Server specified: {args.server}')
        print(f'Port specified {args.port}')
    else:
        print('Server not specified')


main()
