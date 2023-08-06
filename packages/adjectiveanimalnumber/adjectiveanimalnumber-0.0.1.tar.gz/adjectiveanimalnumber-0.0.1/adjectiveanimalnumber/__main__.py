from adjectiveanimalnumber import generate

import argparse

parser = argparse.ArgumentParser(description='Generate a random adjective with an animal name and a random integer.')
parser.add_argument('-a', '--adjs', type=int, default=1, help='Number of adjectives to generate')
parser.add_argument('-s', '--sep', type=str, default='-', help='Separator between adjectives and animal name')
parser.add_argument('-n', '--num', action="store_true", default=False,
                    help='Remove the random integer to the end of the string')
parser.add_argument('-i', '--inf', type=int, default=0, help='Inferior limit for random integer')
parser.add_argument('-u', '--sup', type=int, default=100, help='Superior limit for random integer')


def main():
    args = parser.parse_args()
    aan = generate(args.adjs, args.sep, not args.num, args.inf, args.sup)
    print(aan)


if __name__ == "__main__":
    main()