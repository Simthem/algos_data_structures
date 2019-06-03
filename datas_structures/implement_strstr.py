def implement_str(haystack, needle):

    if (not haystack and not needle) or not needle:
        return 0;
    for i in range(len(haystack)):
        cur = haystack[i:i + len(needle)];
        if cur == needle[0:len(needle)]:
            return i;
    return -1;
