# -*- coding: utf-8 -*-
# @Author: kmrocki
# @Date:   2017-01-01 10:39:24
# @Last Modified by:   kmrocki
# @Last Modified time: 2017-01-01 10:42:50

# There are  lines of numeric input:
# The first line has a double,  (the
# cost of the meal before tax and tip).
cost = input()
# The second line has an integer,  (the
# percentage of  being added as tip).
tip = input()
# The third line has an integer,  (the
# percentage of  being added as tax).
tax = input()

# Print The total meal cost is totalCost
# dollars., where  is the rounded
# integer result of the entire bill (
# with added tax and tip).
tipAmt = cost * tip / 100.0
taxAmt = cost * tax / 100.0
total = round(cost + tipAmt + taxAmt)
print "The total meal cost is %d dollars." % total
