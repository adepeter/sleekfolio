class Choicify:

    def __init__(self, choices):
        self.__choices = sorted(choices)

    def __dictify_choices(self, choices):
        d = dict(choices)
        count = {}
        for k, v in d.items():
            count[k] = len(k)
        return count.values()


    @property
    def get_choices(self):
        return self.__choices

    def __len__(self):
        return max(self.__dictify_choices(self.__choices))