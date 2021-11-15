import myStatsPackage as stats

########### Defining samples ####################

# Sample 1
a = [76, 78, 90, 95, 86, 85, 94, 68, 67, 74, 76, 48]

# Sample 2
b = [4, 2, 3, 1, 6, 8, 1, 7, 8, 10, 11, 10, 15, 16]

# Sample 3
c = [14, 25, 32, 18, 16, 23, 10, 17, 18, 15]

# Sample 4
d = list(range(1, 21, 2))

########### Defining samples ######################

stats.summary(a)

print("\n")

stats.t_one_sample(a)

print("\n")

stats.summary(b)

print("\n")

stats.t_one_sample(b)

print("\n")

stats.t_paired(a, b)

print("\n")

stats.t_paired(a, c)

print("\n")

stats.t_indpt_sample(b, a)

print("\n")

stats.t_indpt_sample(b, a)

print("\n")

stats.f_3groups(a, b, c)
