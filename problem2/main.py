def draw_xyz(N):
    pattern = ""
    if number <= 1 :
        return False
    elif number <= 3:
        return True
    elif number % 2 == 0 or number % 3 == 0 :
        return False
    elif number <= 5:
        return True
    else :
        for i in range(5,9):
            if number % i == 0:
                return False
            return True

if __name__ == '__main__':
    print(draw_xyz(3))
    """
    Y Z X
    Z Y X
    Y Z X
    """


    print(draw_xyz(5))
    """
    Y Z X Z Y
    X Y Z X Z
    Y X Y Z X
    Z Y X Y Z
    X Z Y X Y
    """