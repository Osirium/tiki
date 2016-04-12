import time
import requests
import argparse
import random


def snort():
    requests.get('http://tiki.osirium.net/hid.spi?COM=DI4:')
    time.sleep(1)
    requests.get('http://tiki.osirium.net/hid.spi?COM=DI5:')


def eyes(lr, lg, lb, rr, rg, rb):
    # Maximum value for these is 63, anymore and it breaks with a stupid error
    if max([lr, lg, lb, rr, rg, rb]) > 63:
        print("Value out of range 0-63")
    else:
        requests.get(
            'http://tiki.osirium.net/hid.spi?COM=DM;0;{lr}:DM;1;{lg}:DM;2;{lb}:'.format(
                lr=lr,
                lg=lg,
                lb=lb
            )
        )
        requests.get(
            'http://tiki.osirium.net/hid.spi?COM=DM;3;{rr}:DM;6;{rg}:DM;7;{rb}:'.format(
                rr=rr,
                rg=rg,
                rb=rb
            )
        )


def wink():
    eyes(63, 63, 63, 63, 63, 63)
    eyes(63, 63, 63, 0, 0, 0)
    eyes(63, 63, 63, 63, 63, 63)


def randomeyes():
    lr, lg, lb = random.randint(0, 63), random.randint(0, 63), random.randint(0, 63)
    rr, rg, rb = random.randint(0, 63), random.randint(0, 63), random.randint(0, 63)
    eyes(lr, lg, lb, rr, rg, rb)


def disco(n):
    for i in range(int(n)):
        randomeyes()
        time.sleep(1)


def init_head():
    """
    Unmap the mimics from the Digital Outputs so that they do not revert to D.O. state
    """
    requests.get('http://tiki.osirium.net/hid.spi?COM=CMD0;15:CMD1;15:CMD2;15:CMD3;15:')
    time.sleep(0.5)
    requests.get('http://tiki.osirium.net/hid.spi?COM=CMD4;15:CMD5;15:CMD6;15:CMD7;15:')


def main():
    parser = argparse.ArgumentParser(description='Tiki command line')
    subparsers = parser.add_subparsers(title='action')

    init_parser = subparsers.add_parser('init')
    init_parser.set_defaults(func=init_head)

    snort_parser = subparsers.add_parser('snort')
    snort_parser.set_defaults(func=snort)

    eyes_parser = subparsers.add_parser('eyes')
    eyes_parser.set_defaults(func=eyes)
    eyes_parser.add_argument('lr', default=0, metavar='lr')
    eyes_parser.add_argument('lg', default=0, metavar='lg')
    eyes_parser.add_argument('lb', default=0, metavar='lb')
    eyes_parser.add_argument('rr', default=0, metavar='rr')
    eyes_parser.add_argument('rg', default=0, metavar='rg')
    eyes_parser.add_argument('rb', default=0, metavar='rb')

    wink_parser = subparsers.add_parser('wink')
    wink_parser.set_defaults(func=wink)

    random_parser = subparsers.add_parser('random')
    random_parser.set_defaults(func=randomeyes)

    disco_parser = subparsers.add_parser('disco')
    disco_parser.add_argument('n', default=1, metavar='n')
    disco_parser.set_defaults(func=disco)

    args = parser.parse_args()
    kwargs = dict(args._get_kwargs())
    del kwargs['func']
    args.func(**kwargs)

if __name__ == '__main__':
    main()
