from landmarks_server import ServerAPI

def main():
    server = ServerAPI("127.0.0.1", 8000)
    server.run()

if __name__ == "__main__":
    main()