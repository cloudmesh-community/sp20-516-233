# Holly Zhang sp20-516-233 E.Multipass.2

# testing code

p = Provider()

# TestMultipass.test_provider_run_os
r1 = p.run(command="uname -a", executor="os")
print(r1)
#Linux cloudmesh 4.15.0-74-generic #84-Ubuntu SMP Thu Dec 19 08:06:28 UTC 2019 x86_64 x86_64 x86_64 GNU/Linux

# TestMultipass.test_provider_run_live
r2 = self.provider.run(command="uname -a", executor="live")
print(r2)
#