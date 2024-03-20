init -1 python:
    if persistent.UnlockedGallery is None:
        persistent.UnlockedGallery = []

    class Gallery():
        def __init__(self, name, image, button, ID=None, label=None):
            self.name = name
            self.image = image
            self.button = button
            self.label = label
            self.ID = ID

    #    def anim(self):
    #        if self.tags == "Animation":
    #            return self.image.replace(".webp", "").replace(".png", "")
    #        else:
    #            return "images/HG/" + self.image

    def historyReverse(list):
        newList = []
        for i in list:
            newList.append(i)
        newList.reverse()
        return newList

    def unlock(name):
        persistent.UnlockedGallery.append(name)

    def isUnlocked(part, page, i):
        if page in galleryDict[part] and len(galleryDict[part][page]) >= i+1 and part == "Scenes" and galleryDict[part][page][i].ID in persistent.UnlockedGallery:
            return True
        elif page in galleryDict[part] and len(galleryDict[part][page]) >= i+1 and part == "Images" and type(galleryDict[part][page][i].image) == type([]) and renpy.seen_image(galleryDict[part][page][i].image[0]):
            return True
        elif page in galleryDict[part] and len(galleryDict[part][page]) >= i+1 and part == "Images" and not type(galleryDict[part][page][i].image) == type([]) and renpy.seen_image(galleryDict[part][page][i].image):
            return True
        return False
