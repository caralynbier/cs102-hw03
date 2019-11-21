import sys
from statistics import mean


def main():

    assert len(sys.argv) > 1, "No input file path specified."

    input_file_path = sys.argv[1]
    print(f"Processing input file: {input_file_path}")

    f = open(input_file_path,"r")
    content = f.read()

    arr = content.split("\n")

    for i in range(len(arr)):
        lst = arr[i].split(",")
        num_list = []
        for val in lst:
            if val != '':
                num_list.append(float(val))
        print(mean(num_list))


if __name__ == "__main__":
    main()
