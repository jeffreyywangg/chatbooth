import sys
from client_cli import *
from server import *
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--server', default=False, action='store_true')
parser.add_argument('--servers', type=str)
parser.add_argument('--port', type=int)

parser.add_argument('--server_id', type=str)
parser.add_argument('--leader_id', type=str)
parser.add_argument('--replica_ids', type=str, default="")
parser.add_argument('--replica_urls', type=str, default="")
parser.add_argument('--server_storage', type=str)

args = parser.parse_args()

if args.server:
  if not args.server_id:
    print('Please specify a server ID.')
  elif not args.port:
    print('Please specify a port.')
  else:
    replica_ids = [rid for rid in args.replica_ids.split(',') if rid]
    replica_urls = [url for url in args.replica_urls.split(',') if url]
    if len(replica_ids) != len(replica_urls):
      print('Invalid replica count.')
    else:
      server = Server(
        args.server_id,
        args.leader_id,
        {rid:ReplicaInformation(rid, url) for (rid, url) in zip(replica_ids, replica_urls)},
        args.server_storage
      )
      server.start(args.port)
else:
  cli = ClientCli(args.servers.split(','))
  cli.main()
