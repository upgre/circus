import argparse
import ConfigParser

from circus.workers import Workers


def main():
    parser = argparse.ArgumentParser(description='Run some programs.')
    parser.add_argument('config', help='configuration file')
    args = parser.parse_args()

    cfg = ConfigParser.ConfigParser()
    cfg.read(args.config)
    cmd = cfg.get('circus', 'cmd') + ' ' + cfg.get('circus', 'args')
    check = int(cfg.get('circus', 'check_delay'))
    warmup = int(cfg.get('circus', 'warmup_delay'))
    size = int(cfg.get('circus', 'num-workers'))
    endpoint = cfg.get('circus', 'endpoint')
    workers = Workers(size, cmd, check, warmup, endpoint)
    try:
        workers.run()
    finally:
        workers.terminate()


if __name__ == '__main__':
    main()
