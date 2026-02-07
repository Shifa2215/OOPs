insta = InstagramAccount("shifa_insta", "1234")

insta.add_private_reel("Travel Vlog")
insta.add_private_reel("Food Reel")

insta.add_archived_reel("Old Memories")
insta.add_archived_reel("College Days")

print("\nAs Follower:")
insta.display_private_reels(True)

print("\nAs Non-Follower:")
insta.display_private_reels(False)

print("\nArchived Reels with Wrong Password:")
insta.display_archived_reels("0000")

print("\nArchived Reels with Correct Password:")
insta.display_archived_reels("1234")

print("\nUsing Getter Method:")
print(insta.get_archived_reels("1234"))

insta.set_password("5678")

print("\nArchived Reels After Password Change:")
insta.display_archived_reels("5678")
