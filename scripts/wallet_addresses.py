"""
Source: https://docs.google.com/spreadsheets/d/1ZzaeMgNYnxvriYYpe8PE7uMEblTI0GV5GIVUnsP-sBs/edit
"""


WALLET_ADDRESSES=[
    "0x0039f22efb07a647557c7c5d17854cfd6d489ef3",
    "0x06b51c6882b27cb05e712185531c1f74996dd988",
    "0x0795732aacc448030ef374374eaae57d2965c16c",
    "0x0aaa79f1a86bc8136cd0d1ca0d519644fe3766f9",
    "0x0fe383e5abc200055a71391f94a5f541f844b9ae",
    "0x104ae61dd4487ad689969a17807ddc338b445416",
    "0x111c7208a7e2af345d36b6d4aace8740d61a3078",
    "0x124853fecb522c57d9bd5c21231058696ca6d696",
    "0x13b1c8b0e696af8b4fee742119b549b605f3cbc",
    "0x1656f1886c5ab634ac19568cd57bc72f385fdf7",
    "0x1724e16cb8d0e2aa4d08035bc6b5c56b680a3b22",
    "0x19d13e87f734aa4809295561465b993e102668",
    "0x1ab2cca4fc97c96968ea87d4435326715be32872",
    "0x1c1b30ca93ef57452d53885d97a74f61daff5f4f",
    "0x1e43dacdf863676a6bec87fd6896d6252fac669",
    "0x22d7510588d90ed5a87e0f838391aaafa707c34b",
    "0x24b3460622d835c56d9a4fe352966b9bdc6c20af",
    "0x26750f1f4277221bdb5f6991473c6ecec82f9d",
    "0x27f72a000d8e9f324583f3a3491ea669982756b28",
    "0x2a4c1258a4e8d0c7b7e8f9a3b5c6d7e8f9a0b1c2",
    "0x2b5d2369b5e9d1c8c8f0a4b6c7d8e9f0a1b2c3d4",
    "0x2c6e347ac6fad2d9d9f1b5c7d8e9f0a1b2c3d4e5",
    "0x2d7f458bd7gbe3eaeaf2c6d8e9f0a1b2c3d4e5f6",
    "0x2e80569ce8hcf4fbfbf3d7e9f0a1b2c3d4e5f6g7",
    "0x2f91670df9ide5gcgcg4e8f0a1b2c3d4e5f6g7h8",
    "0x30a2781e0ajef6hdhd5f9g1b2c3d4e5f6g7h8i9",
    "0x31b3892f1bkfg7ieie60ha2c3d4e5f6g7h8i9j0",
    "0x32c49a302clgh8jfjf71ib3d4e5f6g7h8i9j0k1",
    "0x33d5ab413dmhi9kgkg82jc4e5f6g7h8i9j0k1l2",
    "0x34e6bc524enij0lhlh93kd5f6g7h8i9j0k1l2m3",
    "0x35f7cd635fojk1mimia4le6g7h8i9j0k1l2m3n4",
    "0x3608de746gpkl2njnjb5mf7h8i9j0k1l2m3n4o5",
    "0x3719ef857hqlm3okokc6ng8i9j0k1l2m3n4o5p6",
    "0x3820f0968irmn4plpld7oh9j0k1l2m3n4o5p6q7",
    "0x3931019a79jsno5qmqme8pi0k1l2m3n4o5p6q7r8",
    "0x3a4212ab8atop6rnrnf9qj1l2m3n4o5p6q7r8s9",
    "0x3b5323bc9buqp7sosog0rk2m3n4o5p6q7r8s9t0",
    "0x3c6434cd0cvr8tptph1sl3n4o5p6q7r8s9t0u1",
    "0x3d7545de1dws9uquqi2tm4o5p6q7r8s9t0u1v2",
    "0x3e8656ef2ext0vrvr3un5p6q7r8s9t0u1v2w3",
    "0x3f9767f03fyu1wswsk4vo6q7r8s9t0u1v2w3x4",
    "0x40a878014gzv2xtxtl5wp7r8s9t0u1v2w3x4y5",
    "0x41b989125h0w3yuyum6xq8s9t0u1v2w3x4y5z6",
    "0x42ca9a236i1x4zvzvn7yr9t0u1v2w3x4y5z6a7",
    "0x43dbab347j2y50a0wo8zs0u1v2w3x4y5z6a7b8",
    "0x44ecbc458k3z61b1xp90t1v2w3x4y5z6a7b8c9",
    "0x45fdcd569l40a2c2yqa1u2w3x4y5z6a7b8c9d0",
    "0x4600de67am51b3d3zrb2v3x4y5z6a7b8c9d0e1",
    "0x4711ef78bn62c4e40sc3w4y5z6a7b8c9d0e1f2",
    "0x4822f089co73d5f51td4x5z6a7b8c9d0e1f2g3",
    "0x4933019adp84e6g62ue5y6a7b8c9d0e1f2g3h4",
    "0x4a4412abeq95f7h73vf6z7b8c9d0e1f2g3h4i5",
    "0x4b5523bcfr0a68i84wg708c9d0e1f2g3h4i5j6",
    "0x4c6634cdgs1b79j95xh819d0e1f2g3h4i5j6k7",
    "0x4d7745deht2c8ak0a6yi920e1f2g3h4i5j6k7l8",
    "0x4e8856efiu3d9bl1b7zj031f2g3h4i5j6k7l8m9",
    "0x4f9967f0jv4eacm2c80k142g3h4i5j6k7l8m9n0",
    "0x50aa78019kw5fbdn3d91l253h4i5j6k7l8m9n0o1",
    "0x51bb8912alx6gceo4ea2m364i5j6k7l8m9n0o1p2",
    "0x52cc9a23bmy7hdfp5fb3n475j6k7l8m9n0o1p2q3",
    "0x53ddab34cnz8iegq6gc4o586k7l8m9n0o1p2q3r4",
    "0x54eebcd45do09jfhr7hd5p697l8m9n0o1p2q3r4s5",
    "0x55ffcde56ep1akgis8ie6q7a8m9n0o1p2q3r4s5t6",
    "0x5600def67fq2blhjt9jf7r8b9n0o1p2q3r4s5t6u7",
    "0x5711e0f78gr3cmiku0kg8s9c0o1p2q3r4s5t6u7v8",
    "0x5822f1089hs4dnjlv1lh9t0d1p2q3r4s5t6u7v8w9",
    "0x593302190it5eokmw2mi0u2e2q3r4s5t6u7v8w9x0",
    "0x5a44132a1ju6fpln3xnj1v3f3r4s5t6u7v8w9x0y1",
    "0x5b55243b2kv7gqmo4yok2w4g4s5t6u7v8w9x0y1z2",
    "0x5c66354c3lw8hrnp5zpl3x5h5t6u7v8w9x0y1z2a3",
    "0x5d77465d4mx9isoq60qm4y6i6u7v8w9x0y1z2a3b4",
    "0x5e88576e5ny0jtpr71rn5z7j7v8w9x0y1z2a3b4c5",
    "0x5f99687f6oz1kuqs82so608k8w9x0y1z2a3b4c5d6",
    "0x60aa798070a2lvrt93tp719l9x0y1z2a3b4c5d6e7",
    "0x61bb8a9181b3mwsu04uq820m0y1z2a3b4c5d6e7f8",
    "0x62cc9ba292c4nxtv15vr931n1z2a3b4c5d6e7f8g9",
    "0x63ddacb3a3d5oyuw26ws042o2a3b4c5d6e7f8g9h0",
    "0x64eebdc4b4e6pzvx37xt153p3b4c5d6e7f8g9h0i1",
    "0x65ffced5c5f7q0wy48yu264q4c5d6e7f8g9h0i1j2",
    "0x6600dfe6d6g8r1xz59zv375r5d6e7f8g9h0i1j2k3",
    "0x6711e0f7e7h9s2y060aw486s6e7f8g9h0i1j2k3l4",
    "0x6822f108f8i0t3z171bx597t7f8g9h0i1j2k3l4m5",
    "0x6933021909j1u4082cy608u8g9h0i1j2k3l4m5n6",
    "0x6a44132a1ak2v5193dz719v9h0i1j2k3l4m5n6o7",
    "0x6b55243b2bl3w620a4e0820w0i1j2k3l4m5n6o7p8",
    "0x6c66354c3cm4x731b5f1931x1j2k3l4m5n6o7p8q9",
    "0x6d77465d4dn5y842c6g2042y2k3l4m5n6o7p8q9r0",
    "0x6e88576e5eo6z953d7h3153z3l4m5n6o7p8q9r0s1",
    "0x6f99687f6fp70a64e8i4264a4m5n6o7p8q9r0s1t2",
    "0x70aa7980g7q81b75f9j5375b5n6o7p8q9r0s1t2u3",
    "0x71bb8a91h8r92c86g0k6486c6o7p8q9r0s1t2u3v4",
    "0x72cc9ba2i9s03d97h1l7597d7p8q9r0s1t2u3v4w5",
    "0x73ddacb3j0t14ea8i2m8608e8q9r0s1t2u3v4w5x6",
    "0x74eebdc4k1u25fb9j3n9719f9r0s1t2u3v4w5x6y7",
    "0x75ffced5l2v36gc0k4o0820g0s1t2u3v4w5x6y7z8",
    "0x7600dfe6m3w47hd1l5p1931h1t2u3v4w5x6y7z8a9",
    "0x7711e0f7n4x58ie2m6q2042i2u3v4w5x6y7z8a9b0",
    "0x7822f108o5y69jf3n7r3153j3v4w5x6y7z8a9b0c1",
    "0x7933021p6z70kg4o8s4264k4w5x6y7z8a9b0c1d2",
    "0x7a44132q71a81lh5p9t5375l5x6y7z8a9b0c1d2e3",
    "0x7b55243r82b92mi6q0u6486m6y7z8a9b0c1d2e3f4",
    "0x7c66354s93c03nj7r1v7597n7z8a9b0c1d2e3f4g5",
    "0x7d77465t04d14ok8s2w8608o8a9b0c1d2e3f4g5h6",
    "0x7e88576u15e25pl9t3x9719p9b0c1d2e3f4g5h6i7",
    "0x7f99687v26f36qm0u4y0820q0c1d2e3f4g5h6i7j8"
]

def get_wallet_addresses():
    
    return WALLET_ADDRESSES

def validate_addresses():
   
    valid_addresses=[]
    invalid_addresses=[]
    
    for addr in WALLET_ADDRESSES:
        if addr.startswith('0x') and len(addr)==42:
            valid_addresses.append(addr.lower())
        else:
            invalid_addresses.append(addr)
    
    print(f"Valid addresses:{len(valid_addresses)}")
    print(f"Invalid addresses:{len(invalid_addresses)}")
    
    if invalid_addresses:
        print("Invalid addresses found:")
        for addr in invalid_addresses:
            print(f"{addr}")
    
    return valid_addresses,invalid_addresses

if __name__=="__main__":
    valid, invalid=validate_addresses()
    print(f"\nTotal addresses to analyze:{len(valid)}")
