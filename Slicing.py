planet1="Closest of Sun"
print(planet1)

print(planet1[0])
print(planet1[1])
print(planet1[2])
print(planet1[5])

print(planet1[-1])
print(planet1[-2])
print(planet1[-3])
print(planet1[-4])

# Slicing a string, get a substring from a string

print(planet1[1:4])
print(planet1[:7])
print(planet1[12:])
print(planet1[11:])


#  Slicing Tuple
devops=("Linux", "Vagrant","Bash Scripting", "AWS", "Jenkins","Python", "Ansible" )

print(devops[0])        # It will print Linux
print(devops[3])        # It will print AWS
print(devops[-1])       # It will print  Ansible

print(devops[2:5])        # It will print Bash Scripting, AWS, Jenkins
print(devops[2:5][0])     # It will print Bash Scripting

print(devops[2:5][0][5:11])   # It will print Script

print(devops[2:5][0][5:11][-1]) # It will print t


# Slicing List
devops=["Linux", "Vagrant","Bash Scripting", "AWS", "Jenkins","Python", "Ansible" ]

print(devops[0])          # It will print Linux
print(devops[3])          # It will print AWS
print(devops[-1])         # It will print  Ansible

print(devops[2:5])             # It will print Bash Scripting, AWS, Jenkins
print(devops[2:5][0])          # It will print Bash Scripting

print(devops[2:5][0][5:11])    # It will print Script

print(devops[2:5][0][5:11][-1]) # It will print t



# Dictionary Example
skills={"DevOps":("AWS", "Jenkins","Python", "Ansible"), "Development":["Java","NodeJS", ".net"]}
print(skills)  # It print {'DevOps': ('AWS', 'Jenkins', 'Python', 'Ansible'), 'Development': ['Java', 'NodeJS', '.net']}

print(skills["DevOps"])          # It prints ('AWS', 'Jenkins', 'Python', 'Ansible')
print(skills["Development"])     # It prints ['Java', 'NodeJS', '.net']
print(skills["DevOps"][-1])      # It prints Ansible
print(skills["DevOps"][-1][:3])  # It prints Ans

