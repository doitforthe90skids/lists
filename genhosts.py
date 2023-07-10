file = open('hosts-rev230709.txt', 'r')

for i in range(1,600):
    print('echo. >> C:\\\Windows\\\System32\\\drivers\\\etc\\\hosts')

for line in file:
    if '#' not in line:
        raw = line.strip()
        print('echo %s >> C:\\\Windows\\\System32\\\drivers\\\etc\\\hosts' % (raw))
