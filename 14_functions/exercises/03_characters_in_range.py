def main():
    def chr_in_range(chr1, chr2):
        lst = []
        for i in range(ord(chr1) + 1, ord(chr2)):
            lst.append(chr(i))
        return lst

    char_1 = input()
    char_2 = input()
    print(*chr_in_range(char_1, char_2))


main()
