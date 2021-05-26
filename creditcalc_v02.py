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

check = [args.type, args.principal, args.payment, args.periods, args.interest]
counter = 0

for i in check:
    if i is None:
        counter += 1

if counter == 5:
    pass
elif args.type is None or args.type not in ["annuity", "diff"]:
    print("Incorrect parameters")
elif args.type == "diff" and args.payment:
    print("Incorrect parameters")
elif len(sys.argv) != 5:
    print("Incorrect parameters")
elif args.interest is None:
    print("Incorrect parameters")
else:
    for i in sys.argv[2:]:
        if int(i.split("=")[-1]) < 0:
            print("Incorrect parameters")
