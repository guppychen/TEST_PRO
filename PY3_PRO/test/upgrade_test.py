import re

def get_upgrade_version(url):
    # enhance by llin 2017.8.8 in case the URL can not be matched.
    match = re.search(r'.*?browse/(.*?)/artifact.*', url)
    match = re.search(r'.*?artifact/(.*?)/shared/build(.*?)/.*', url)
    targetBuildId = ""
    if match != None:
        print("** Get upgrade build number is: %s **"%(match.group(1)+match.group(2)))
        targetBuildId = match.group(1)+match.group(2)
    else:
        print( "!! upgrade can not match the build from URL !!" )
        print( "!! current URL is: %s !!"%(url) )

    print(targetBuildId)
    return targetBuildId

def main():
    url = 'http://bamboo.calix.local/artifact/IBAXOS194-CI/shared/build-610/FullRelease.run/FullRelease_system-E7-2_IB-AXOS-19.4_20191008211023_builder.run'
    build = get_upgrade_version(url)


if __name__ == '__main__':
    main()