from db import seeding_v1


def seed():
    seeding_v1.seed_user()
    seeding_v1.seed_closet()
    seeding_v1.seed_clothes()


if __name__ == "__main__":
    seed()
