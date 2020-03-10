#!/usr/bin/env python
import optparse, random, os # import modules

#To parse command line
usage = "usage: %prog [options]"
p = optparse.OptionParser(usage)

p.add_option('-s', '--students', help='File containing student names, one per line [None, Required]')
p.add_option('-p', '--projects', help="File containing project info. tsv: one line per project. First column is lead student's name, second is project's name [None, Required]")
p.add_option('-n', '--num', type='int', default=4, help='Target number of students per group. [None, Required]')

opts, args = p.parse_args()

# Read in list of student names
with open(opts.students, "r") as in_file: lines = [l.strip() for l in in_file.readlines() if l.strip()]

# Make project dict
proj_dict = {}
group_dict = {}
with open(opts.projects, "r") as in_file:
    for line in in_file:
        cols = line.strip().split('\t')
        proj_dict[cols[0]] = cols[1]
        group_dict[cols[1]] = []
        
# randomizes list in place
random.shuffle(lines) 

# Creates a list of list from the shuffled input list
groups = [ lines[i:i+opts.num] for i in range(0, len(lines), opts.num) ] 

# Reshuffle if multiple project leads are in the same group
multiLead = {i:list(set(g).intersection(set(proj_dict.keys()))) for i,g in enumerate(groups) if len(set(g).intersection(set(proj_dict.keys())))>1}
if multiLead:
#    print 'Reshuffle'
    noLead = [i for i,g in enumerate(groups) if not set(g).intersection(set(proj_dict.keys()))]
    for each in multiLead:
        focalLeads = multiLead[each][:]
        while len(focalLeads)>1:
            swapInd = noLead.pop(random.choice(range(len(noLead))))
            studSwap = groups[swapInd].pop(random.choice(range(len(groups[swapInd]))))
            leadSwap = focalLeads.pop(random.choice(range(len(focalLeads))))
            del(groups[each][groups[each].index(leadSwap)])
            groups[swapInd].append(leadSwap)
            groups[each].append(studSwap)

#If the length of the last group is more than one less than the target, move students around
i=-2
while len(groups[-1]) < opts.num-1: 
    groups[-1].append(groups[i].pop())
    i-=1

for g in groups:
    match=0
    for s in g:
        if s in proj_dict:
            group_dict[proj_dict[s]].append(", ".join(g))
            match=1
            continue
    if not match: group_dict[random.choice(group_dict.keys())].append(", ".join(g))

# Redistribute, if needed
while [1 for x in group_dict.values() if len(x)<2]:
#    print 'Redistribute'
    underRep = [p for p,x in group_dict.items() if len(x)<2]
    overRep = [p for p,x in group_dict.items() if len(x)>2]
    for each in underRep:
        donor = random.choice(overRep)
        toMove = group_dict[donor].pop(random.choice(range(len(group_dict[donor]))))
        while set(toMove.split(", ")).intersection(set(proj_dict.keys())):
            group_dict[donor].append(toMove)
            toMove = group_dict[donor].pop(random.choice(range(len(group_dict[donor]))))
        group_dict[each].append(toMove)

# Print and write out groups
with open("grouped_by_{}_".format(opts.num).join(os.path.split(opts.students)), "w" ) as out_file: 
    for project, gs in group_dict.iteritems():
        print "\n%s:\n\t%s" % (project, "\n\t".join(gs))
        out_file.write("\n%s:\n\t%s\n" % (project, "\n\t".join(gs)))
