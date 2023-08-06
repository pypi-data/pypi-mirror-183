'''
Notice: Currently this will generate around 36,205,000 possible emails if all flags are enabled
'''
import os, sys

help_flag = "-h"
host_flag = "-d"
generate_flag = "-g"
size_flag = "-s"
years_flag = "-y"
numbers_flag = "-n"
output_flag = "-o"
wordlist_flag = "-w"
distribute_flag = "-b"

def display_help():
    help_messages = [
        f"{help_flag} for help",
        f"{generate_flag} to generate a new bulk list",
        f"{size_flag} to set chunk size DEFAULT:20000",
        f"{host_flag} to enter a cvs list of desired email hosts DEFAULT: gmail.com, hotmail.com, outlook.com",
        f"{numbers_flag} to include numbers 0-100 to cover common sports numbers and year abbreviations that may are likely to be included in email",
        f"{years_flag} to include years 1950-2050 for common graduation/birth years in email",
        f"{wordlist_flag} to include a wordlist of usernames to use instead of most popular names",
        f"{distribute_flag} to distribute the existing generated list into smaller files. Set filesize using the {size_flag} flag"
    ]

    for msg in help_messages:
        print(f"\t{msg}")

def get_names():
    first_names = ["james", "robert", "michael", "david", "william", "richard", 
        "dick", "joseph", "joe", "thomas", "tom", "charles", "chuck", "christopher", "chris",
        "matthew", "matt", "anthony", "tony", "mark", "donald", "don", "steven", "steve", "paul",
        "andrew", "drew", "joshua", "josh", "kenneth", "ken", "kenny", "kevin", "brian", "george",
        "timothy", "tim", "ronald", "ron", "edward", "ed", "jason", "jeffrey", "jeff", "ryan", "jacob", "jake",
        "gary", "nicholas", "nick", "eric", "erik", "jonathan", "jon", "john", "stephen", "larry", "justin", "scott",
        "brandon", "benjamin", "ben", "samuel", "sam", "gregory", "greg", "alexander", "alex", "frank", "patrick", "rick",
        "raymond", "ray", "jack", "jackson", "dennis", "jerry", "tyler", "aaron", "jose", "adam", "nathan", "nate", "henry",
        "douglas", "doug", "zachary", "zach", "zack", "peter", "pete", "kyle", "ethan", "walter", "noah", "jeremy",
        "christian", "keith", "roger", "terry", "gerald", "harold", "sean", "shawn", "austin", "carl", "arthur",
        "lawrence", "dylan", "jesse", "jesse", "jordan", "bryan", "billy", "bruce", "gabriel", "gabe", "logan",
        "albert", "al", "willie", "willy", "alan", "juan", "wayne", "elijah", "eli", "randy", "roy", "vincent", "vince",
        "ralph", "eugene", "russell", "russ", "bobby", "mason", "philip", "phil", "phillip", "louis", "lou", "louie", "lewis",
        "logan", "devin", "dorian",
        "mary", "patricia", "pat", "pattie", "jennifer", "jenny", "jen", "linda", "elizabeth", "liz", "beth", "barbara", "barb",
        "susan", "sue", "jessica", "jess", "sarah", "sara", "karen", "lisa", "nancy", "betty", "margaret", "sandra", "ashley",
        "kimberly", "emily", "donna", "michelle", "carol", "amanda", "dorothy", "melissa", "deborah", "stephanie", "rebecca",
        "sharon", "laura", "cynthia", "kathleen", "amy", "angela", "shirley", "anna", "brenda", "pamela", "emma", "nicole",
        "helen", "samantha", "sam", "katherine", "kat", "christine", "debra", "rachel", "carolyn", "janet", "catherine",
        "maria", "heather", "diane", "ruth", "julie", "olivia", "joyce", "virginia", "victoria", "kelly", "lauren",
        "christina", "joan", "evelyn", "judith", "megan", "andrea", "cheryl", "hannah", "jacqueline", "jackie", "martha",
        "gloria", "teresa", "ann", "anne", "madison", "frances", "kathryn", "janice", "jean", "abigail", "abby",
        "alice", "julia", "judy", "sophia", "sophie", "grace", "denise", "amber", "doris", "marilyn", "danielle",
        "beverly", "bev", "isabelle", "belle", "theresa", "diana", "natalie", "brittany", "charlotte", "marie",
        "kayla", "alexis", "lori"] #https://www.ssa.gov/oact/babynames/decades/century.html
    
    last_names = ["wang", "smith", "devi", "ivanov", "kim", "ali", "garcia", "muller", "silva", "dasilva", "mohammed",
        "tesfaye", "nguyen", "ilunga", "gonzalez", "deng", "rodriguez", "moyo", "hansen", "zhang", "johnson", "williams",
        "brown", "jones", "anderson", "hernandez", "lopez", "miller", "chavez", "davis", "wilson", "thomas", "taylor",
        "moore", "jackson", "martin", "lee", "perez", "thompson", "white", "haris", "sanchez", "clark", "ramirez",
        "lewis", "robinson", "walker", "young", "allen", "king", "right", "scott", "torres", "hill", "flores", "green",
        "adams", "nelson", "baker", "hall", "rivera", "campbell", "mitchell", "carter", "roberts", "gomez", "phillips",
        "evans", "turner", "diaz", "parker", "cruz", "edwards", "collins", "reyes", "stewart", "morris", "morales",
        "murphy", "cook", "rogers", "gutierrez", "ortiz", "morgan", "cooper", "peterson", "bailey", "reed", "kelly",
        "howard", "ramos", "kim", "cox", "ward", "richardson", "watson", "brooks", "chavez", "wood", "james",
        "bennet", "grey", "mendoza", "ruiz", "hughes", "price", "alvarez", "catillo", "sanders", "patel", "myers", 
        "ross", "foster", "jimenez"] #https://www.thoughtco.com/most-common-us-surnames-1422656
    
    return [(a, b) for a in first_names for b in last_names]

def create_email_usernames(name_pair, include_numbers, include_years):
    if (type(name_pair) is tuple) or (type(name_pair) is list):
        possible_combinations = [f"{name_pair[0]}{name_pair[1]}", f"{name_pair[0]}.{name_pair[1]}"]

        if include_numbers:
            #cover smaller numbers like sports numbers and abbreviated years
            for i in range(0,100):
                possible_combinations.append(f"{name_pair[0]}.{name_pair[1]}{i}")
                possible_combinations.append(f"{name_pair[0]}{name_pair[1]}{i}")
        
        if include_years:
            #cover from 1950-2050 for birth years and grad years
            for i in range(1950, 2050):
                possible_combinations.append(f"{name_pair[0]}.{name_pair[1]}{i}")
                possible_combinations.append(f"{name_pair[0]}{name_pair[1]}{i}")

        return possible_combinations
    else:
        return name_pair

def write_file(storage_path, data, chunk_count):
    filename = f"{storage_path}email_list_{chunk_count}.txt"
    with open(filename, "w") as nf:
        nf.writelines(data)

def read_wordlist(path):
    names = []
    with open(path, "r") as f:
        for l in f.readlines():
            names.append(l)
    return names

def distribute_emails(file_path, storage_path, chunk_size): 
    chunk_count = 1
    line_count = 0

    try:
        with open(file_path, "r") as f:
            buffered_string = ""
            for line in f.readlines():
                if line_count < int(chunk_size):
                    buffered_string += line
                    line_count += 1
                else:
                    write_file(storage_path, buffered_string, chunk_count)
                    buffered_string = ""
                    line_count = 0
                    chunk_count += 1
            write_file(storage_path, buffered_string, chunk_count) #This writes the last of the buffer to a final file
        return 1
    except FileNotFoundError:
        print("Email list file not found. Please use -g flag to generate a new one.")
        return -1
    except Exception as e:
        print("An unexpected error ocurred when breaking up the existing email list")
        print(e)
        return -1

def generate_email_list(
    file_path, 
    storage_path, 
    use_wordlist, 
    wordlist_path, 
    use_default_hosts, 
    user_hosts, 
    include_years, 
    include_numbers):
    
    all_possible_names = []

    try:
        if use_wordlist:
            all_possible_names = read_wordlist(wordlist_path)
        else:
            all_possible_names = get_names()

        hosts = ["gmail.com", "outlook.com", "hotmail.com"]

        if not use_default_hosts:
            hosts = user_hosts.split(',')

        if not os.path.exists(storage_path):
            os.mkdir(storage_path)
            
        buffer = []
        for names in all_possible_names:
            if (type(all_possible_names[0]) is tuple) or (type(all_possible_names[0]) is list):
                for name in create_email_usernames(names, include_numbers, include_years):
                    for host in hosts:
                        buffer.append(f"{name}@{host}\n")
            else:
                name = str(names).strip("\n")
                for host in hosts:
                    buffer.append(f"{name}@{host}\n")

        with open(file_path, "w") as f:
            f.writelines(buffer)

        return 1
    except:
        print("An unexpected error ocurred generating the email list")
        return -1

def main(
    storage_path = f"{os.getcwd()}/emails/",
    generated_file_path = f"{os.getcwd()}/emails/generated_emails.txt",
    chunk_size = 20000,
    use_default_hosts = True,
    user_hosts = "",
    include_years = False,
    include_numbers = False,
    use_wordlist = False,
    wordlist_path = "",
    test_flag_create=False,
    test_flag_distribute=False):

    if len(sys.argv) > 1:
        if help_flag in sys.argv:
            display_help()
            return 1

        if host_flag in sys.argv:
            if not generate_flag in sys.argv:
                print(f"You must use the {generate_flag} flag to use the {host_flag} flag")
                return -1

            use_default_hosts = False
            user_hosts = sys.argv[sys.argv.index(host_flag) + 1]

        if output_flag in sys.argv:
            output_dir = sys.argv[sys.argv.index(output_flag) + 1]
            if not os.path.exists(output_dir):
                os.mkdir(output_dir)
            storage_path = output_dir
            generated_file_path = f"{storage_path}generated_emails.txt"

        if size_flag in sys.argv:
            chunk_size = sys.argv[sys.argv.index(size_flag) + 1]

        if numbers_flag in sys.argv:
            include_numbers = True

        if years_flag in sys.argv:
            include_years = True

        if wordlist_flag in sys.argv:
            use_wordlist = True
            wordlist_path = sys.argv[sys.argv.index(wordlist_flag) + 1]

        if (generate_flag in sys.argv) or test_flag_create:
            print("Generating email list...")
            return generate_email_list(
                generated_file_path, 
                storage_path, 
                use_wordlist,
                wordlist_path, 
                use_default_hosts, 
                user_hosts,
                include_years,
                include_numbers
            )

        if (distribute_flag in sys.argv) or test_flag_distribute:
            print("Breaking up existing email list...")
            return distribute_emails(generated_file_path, storage_path, chunk_size)

        print("It doesn't look like you used a flag I know. Use -h to get help")
        return -1
    else:
        display_help()
        return -1