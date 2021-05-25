import sys
import argparse

parser = argparse.ArgumentParser(
    formatter_class=argparse.RawDescriptionHelpFormatter,
    description=("""This loan calculator can compute the following. \
\n-----------------------------------------------
  - Your loans annuity monthly payment amount.
  - Your number of monthly payments due.
  - Your loan principal.
  - Your differentiated payments."""))

parser.add_argument("-t", "--type",
                    help="You need to choose from either option: \
                    - annuity: for annuity options. \
                    - diff: for the differentiated payments.")

parser.add_argument("-l", "--principal", type=float,
                    help="The amount being borrowed.")

parser.add_argument("-p", "--payment", type=float,
                    help="The monthly payment due on the loan.")

parser.add_argument("-n", "--periods", type=float,
                    help="The time between the first payment on a loan and \
                    its maturity.")

parser.add_argument("-i", "--interest", type=float,
                    help="The amount charged on top of the principal.")

args = parser.parse_args()

if args.type is None or args.type not in ["annuity", "diff"]:
    print("Incorrect parameters conditions 1")
elif args.type == "diff" and args.payment:
    print("Incorrect parameters conditions 2")
elif len(sys.argv) != 5:
    print("Incorrect parameters conditions 3")
elif args.interest is None:
    print("Incorrect parameters conditions 4")
elif args.principal < 0 or args.periods < 0 or args.interest < 0:
    print("Incorrect parameters conditions 5")
elif args.payment < 0 or args.periods < 0 or args.interest < 0:
    print("Incorrect parameters conditions 6")

'''
args_amount = sys.argv
print(args_amount[2:])
print(len(args_amount))


elif args.principal < 0:
    print("Incorrect parameters conditions 4")

elif args.payment < 0:
    print("Incorrect parameters conditions 5")

elif args.periods < 0:
    print("Incorrect parameters conditions 6")

elif args.interest < 0:
    print("Incorrect parameters conditions 7")


print(args.type)
print(type(args.type))
print(args.payment)
print(type(args.payment))
print(args.principal)
print(type(args.principal))
print(args.periods)
print(type(args.periods))
print(args.interest)
print(type(args.interest))

'''
