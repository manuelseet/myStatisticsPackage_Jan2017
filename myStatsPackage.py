
"""
@author: Manuel Seet
@description: This package calculates various descriptive statistics 
and some hypothesis test values for samples

-- personal python project
"""


# Defining basic functions ###################3

import math


def subtract_listwise(x, y):
    subtract = [x - y for x, y in zip(x, y)]
    return subtract


def name(*variables):
    return [i for i in variables]


def sample_title(x):
    return "============== SAMPLE {} ==============".format(name(x))


##################### Defining distributions #######################


def t(x, df):
    if df > 0:
        return (math.gamma((df+1)/2))/(math.sqrt(math.pi*df) * math.gamma(df/2) * (1+x**2/df)**((df+1)/2))

################# Defining descriptive statistics functions #############


def n(x):
    return len(x)


def mean(x):
    mn = sum(x) / n(x)
    return mn


def median(x):
    ordered_sample = sorted(x)
    if len(x) % 2 == 0:
        middle_first = ordered_sample[int((len(x)/2)-1)]
        middle_second = ordered_sample[int((len(x)/2))]
        middle_two = (middle_first + middle_second)/2
        return middle_two
    else:
        middle_exact = ordered_sample[int((len(x)+1)/2)-1]
        return middle_exact


def sum_sq(x):
    sum_of_sq = sum((i-mean(x))**2 for i in x)
    return sum_of_sq


def variance(x):
    var = sum_sq(x)/(n(x)-1)
    return var


def sd(x):
    std_dev = variance(x)**(0.5)
    return std_dev


def se(x):
    std_err = sd(x) / (n(x))**(0.5)
    return std_err


def summary(x):
    print("### PRINTING SUMMARY STATISTICS OF SAMPLE ###")
    print("Sample is", str(x))
    print("Sample size = ", str(n(x)))
    print("Mean = ", str(round(mean(x), 3)))
    print("Median = ", str(median(x)))
    print("Sum of Squares = ", str(round((sum_sq(x)), 3)))
    print("Variance = ", str(round(variance(x), 3)))
    print("Standard Deviation = ", str(round(sd(x), 3)))
    print("### END OF SUMMARY ###")

########### Defining inferential statistics functions #############


def t_one_sample(x):  # t value; x is sample array ; y is comparison value (default = 0)
    print("SINGLE-SAMPLED T-TEST (to 3 d.p.)")
    print("Sample mean = {}".format(round(mean(x), 3)))
    y = int(input("Enter comparison value: "))
    tv = (mean(x) - y)/se(x)
    df1 = len(x) - 1
    #p = t(abs(tv), df1)
    print("H_o: mu equals to {}".format(y))
    print("H_a: mu not equals to {}".format(y))
    print("t_obs = {}".format(round(tv, 3)), ", df = {}".format(df1))
    #print ("p-value = {}".format(round(p,3)))


def t_indpt_sample(x, y):
    print("INDEPENDENT SAMPLES T-VALUE (to 3 d.p.)")
    print("Sample mean 1 = {}".format(round(mean(x), 3)),
          "Sample mean 2 = {}".format(round(mean(y), 3)))
    print("Sample variance 1 = {}".format(round(variance(x), 3)),
          "Sample variance 2 = {}".format(round(variance(y), 3)))
    assump = input("Assume equality of variance? [print 'y' or 'n']: ")
    if assump == "y":
        df1 = n(x) - 1
        df2 = n(y) - 1
        df_pooled = df1 + df2
        sd1 = sd(x)
        sd2 = sd(y)
        sd_pooled = ((df1*(sd1**2) + df2*(sd2**2))/(df1+df2))**(0.5)
        se_pooled = sd_pooled*(((1/n(x)) + (1/n(y)))**(0.5))
        tv = (mean(x) - mean(y))/se_pooled
        #p = t(abs(tv), df_pooled)
        print("H_o: mu1 equals to mu2")
        print("H_a: mu1 not equals to mu2")
        print("t_obs = {}".format(round(tv, 3)), ", df = {}".format(df_pooled))
        #print ("p-value = {}".format(round(p,3)))
    elif assump == "n":
        df1 = n(x) - 1
        df2 = n(y) - 1
        sd1 = sd(x)
        sd2 = sd(y)
        df_unpooled = ((((sd1**2)/n(x)) + ((sd2**2)/n(y)))**(2)) / \
            (((1/df1)*(((sd1**2)/n(x))**2))+((1/df2)*(((sd2**2)/n(y))**2)))
        se_unpooled = (((sd1**2)/n(x)) + ((sd2**2)/n(y)))**(0.5)
        tv = (mean(x) - mean(y))/se_unpooled
        #p = t(abs(tv), df_unpooled)
        print("H_o: mu1 equals to mu2")
        print("H_a: mu1 not equals to mu2")
        print("t_obs = {}".format(round(tv, 3)),
              ", df = {}".format(round(df_unpooled, 2)))
        print("[simplified df = {}]".format(min(df1, df2)))
        #print ("p-value = {}".format(round(p,3)))
    else:
        print("Unknown input. Run again")


def t_paired(x, y):
    print("DEPENDENT SAMPLES T-VALUE (to 3 d.p.)")
    if n(x) == n(y):
        z = subtract_listwise(x, y)
        print("Sample mean 1 = {}".format(round(mean(x), 3)),
              "Sample mean 2 = {}".format(round(mean(y), 3)))
        tv = (mean(z))/se(z)
        df1 = len(z) - 1
        p = t(abs(tv), df1)
        print("H_o: mu1 equals to mu2")
        print("H_a: mu1 not equals to mu2")
        print("t_obs = {}".format(round(tv, 3)), ", df = {}".format(df1))
        #print ("p-value = {}".format(round(p,3)))
    else:
        print("Sample size 1 = {}".format(n(x)),
              "Sample size 2 = {}".format(n(y)))
        print("Sample size not equal. UNABLE TO PROCEED")


def f_3groups(x, y, z):
    print("INDEPENDENT SAMPLES ANOVA (to 3 d.p.)")
    print("Sample mean 1 = {}".format(round(mean(x), 3)), ", Sample mean 2 = {}".format(
        round(mean(y), 3)), ", Sample mean 3 = {}".format(round(mean(z), 3)))
    whole_sample = x + y + z
    grand_mean = mean(whole_sample)
    j = 3
    dfB = j - 1
    dfT = len(whole_sample) - 1
    dfW = dfT - dfB
    SST = sum_sq(whole_sample)
    SSB = j*((mean(x) - grand_mean)**2 + (mean(y) - grand_mean)
             ** 2 + (mean(z) - grand_mean)**2)
    SSW = SST - SSB
    MSB = SSB / dfB
    MSW = SSW / dfW
    F = MSB / MSW
    print("H_o: mu1 = mu2 = mu3 = 0")
    print("H_a: at least one mu is different")
    print("\n")
    print("F Tables")
    print("___Source___", "___Sum of Sq___", "___df___", "___MS___")
    print("  Between   ", "    {}    ".format(round(SSB, 1)),
          "    {}  ".format(dfB), "      {} ".format(round(MSB, 1)))
    print("  Within    ", "    {}    ".format(round(SSW, 1)),
          "   {}  ".format(dfW), "   {} ".format(round(MSW, 1)))
    print("______________________________________________")
    print("F_obs = {}".format(round(F, 3)),
          ", dfB = {}".format(dfB), ", dfW = {}".format(dfW))
