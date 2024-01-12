data = {}

data['customers'] = ("INSERT INTO `customers` (`mobile_no`, `name`, `address`, `email`, `dues`) VALUES "
                     "(7015984263, 'Anjali Patel', 'G-201, Janakpuri, Delhi 110058', 'anjalipatel345@yahoo.com', 0.00), "
                     "(7108324962, 'Akshay Kumar', 'P-190, Preet Vihar, Delhi 110092', 'akshay.kumar1995@gmail.com', 0.00), "
                     "(7236549810, 'Karan Singh', 'J-56, Pitampura, Delhi 110034', 'karansingh123@rediffmail.com', 0.00), "
                     "(7503148962, 'Amit Gupta', 'D-45, Defence Colony, Delhi 110024', 'amitgupta78@rediffmail.com', 0.00), "
                     "(7632910584, 'Priyanka Kapoor', 'M-308, Ashok Nagar, Delhi 110020', 'priyanka.kapoor2000@hotmail.com', 0.00), "
                     "(7750123698, 'Anu Agarwal', 'S-416, Rajender Nagar, Delhi 110058', 'anu.agarwal786@outlook.com', 0.00), "
                     "(8026493715, 'Sarika Patel', 'O-562, Paschim Vihar, Delhi 110063', 'sarika.patel86@outlook.com', 0.00), "
                     "(8154796320, 'Sara Khan', 'I-42, Saket, Delhi 110017', 'soniakhan@hotmail.com', 0.00), "
                     "(8290561347, 'Rajiv Jain', 'L-241, Dwarka Sector 23, Delhi 110075', 'rajiv.jain72@yahoo.com', 0.00), "
                     "(8302985476, 'Vikram Singh', 'R-349, Greater Kailash I, Delhi 110048', 'vikram.singh54@rediffmail.com', 0.00), "
                     "(8452176390, 'Vikas Sharma', 'F-112, Rajouri Garden, Delhi 110027', 'vikas.sharma@gmail.com', 0.00), "
                     "(8826359741, 'Neha Singh', 'C-32, Greater Kailash II, Delhi 110048', 'nehasingh12@hotmail.com', 0.00), "
                     "(9286571430, 'Sunil Malhotra', 'T-523, Janakpuri District Centre, Delhi 110058', 'sunil.malhotra@gmail.com', 0.00), "
                     "(9375106248, 'Mohan Das', 'N-435, Malviya Nagar, Delhi 110017', 'mohandas1985@rediffmail.com', 0.00), "
                     "(9563218740, 'Rohit Verma', 'H-315, Mayur Vihar Phase I, Delhi 110091', 'rohitverma1990@gmail.com', 0.00), "
                     "(9641730589, 'Ritu Yadav', 'Q-274, Tilak Nagar, Delhi 110018', 'ritu.yadav@hotmail.com', 0.00), "
                     "(9704385126, 'Mansi Chauhan', 'K-178, Rohini Sector 7, Delhi 110085', 'mansi.chauhan97@gmail.com', 0.00), "
                     "(9811234567, 'Riya Sharma', 'A-154, Vasant Kunj, Delhi 110070', 'riya.sharma23@gmail.com', 0.00), "
                     "(9910145268, 'Rahul Kumar', 'B-206, Lajpat Nagar IV, Delhi 110024', 'rahulkumar89@yahoo.com', 0.00), "
                     "(9958623147, 'Priya Mehta', 'E-98, Punjabi Bagh, Delhi 110026', 'priyamehta91@outlook.com', 0.00)")

data['p_id'] = ("INSERT INTO `p_id` (`id`) VALUES "
                "(10001), (10002), (10003), (10004), (10005), (10006), (10007), (10008), (10009), (10010), "
                "(10011), (10012), (10013), (10014), (10015), (10016), (10017), (10018), (10019), (10020), "
                "(10021), (10022), (10023), (10024), (10025), (10026), (10027), (10028), (10029), (10030), "
                "(10031), (10032), (10033), (10034), (10035), (10036), (10037), (10038), (10039), (10040), "
                "(10041), (10042), (10043), (10044), (10045), (10046), (10047), (10048), (10049), (10050), "
                "(10051), (10052), (10053), (10054), (10055), (10056), (10057), (10058), (10059), (10060), "
                "(10061), (10062), (10063), (10064)")

data['stock'] = ("INSERT INTO `stock` (`id`, `desc`, `qty`, `MRP`, `price`, `GST`, `last_updated`, `initial_qty`) VALUES "
                 "(10001, 'Saffola Masala Oats (500g)', 30, 140.00, 110.00, 0, '2024-01-01 10:15:00', 30), "
                 "(10002, 'Surf Excel Matic Powder (1kg)', 54, 250.00, 180.00, 18, '2024-01-01 13:20:00', 54), "
                 "(10003, 'Patanjali Honey (500g)', 22, 200.00, 180.00, 0, '2024-01-01 13:28:00', 22), "
                 "(10004, 'Aashirvaad Sooji (5kg)', 25, 350.00, 285.00, 5, '2024-01-01 15:23:00', 25), "
                 "(10005, 'Haldiram Bhujia (200g)', 37, 180.00, 150.00, 12, '2024-01-01 20:45:00', 37), "
                 "(10006, 'Colgate Total Toothpaste (200g)', 60, 150.00, 132.00, 12, '2024-01-02 10:57:00', 60), "
                 "(10007, 'Himalaya Honey (1kg)', 26, 800.00, 720.00, 0, '2024-01-02 10:58:00', 26), "
                 "(10008, 'Lipton Green Tea (500g)', 29, 220.00, 185.00, 5, '2024-01-02 12:27:00', 29), "
                 "(10009, 'Dabur Vatika Hair Oil (200ml)', 57, 250.00, 210.00, 0, '2024-01-02 12:33:00', 57), "
                 "(10010, 'Tata Tea Gold (100g pack of 10)', 29, 1000.00, 810.00, 5, '2024-01-02 16:40:00', 29), "
                 "(10011, 'Colgate Sensitive Toothpaste (100g)', 63, 120.00, 105.00, 12, '2024-01-02 18:44:00', 63), "
                 "(10012, 'Nestle Munch Chocolates (50g pack of 5)', 28, 125.00, 100.00, 18, '2024-01-02 18:50:00', 28), "
                 "(10013, 'Fortune Basmati Rice (1kg)', 41, 250.00, 195.00, 5, '2024-01-02 20:42:00', 41), "
                 "(10014, 'Amul Ice Cream (500ml cup)', 51, 200.00, 160.00, 18, '2024-01-03 09:43:00', 51), "
                 "(10015, 'Himalaya Apple Cider Vinegar (500ml)', 21, 150.00, 130.00, 5, '2024-01-03 13:18:00', 21), "
                 "(10016, 'Himalaya Neem Face Wash (100ml)', 57, 150.00, 120.00, 18, '2024-01-03 15:04:00', 57), "
                 "(10017, 'Amul Paneer Cubes (200g)', 34, 100.00, 90.00, 5, '2024-01-03 15:22:00', 34), "
                 "(10018, 'Dabur Chyawanprash (500g)', 44, 350.00, 280.00, 18, '2024-01-03 17:11:00', 44), "
                 "(10019, 'Horlicks Classic Malt (500g)', 52, 350.00, 280.00, 18, '2024-01-03 18:32:00', 52), "
                 "(10020, 'Dettol Antiseptic Liquid (200ml)', 48, 175.00, 132.00, 18, '2024-01-03 20:22:00', 48), "
                 "(10021, 'Vim Dishwashing Liquid (500ml)', 20, 75.00, 55.00, 18, '2024-01-04 10:06:00', 20), "
                 "(10022, 'Dettol Antiseptic Liquid Refill (100ml)', 42, 150.00, 110.00, 18, '2024-01-04 10:08:00', 42), "
                 "(10023, 'Nutella Hazelnut Spread (400g)', 52, 350.00, 8, 18, '2024-01-04 12:49:00', 52), "
                 "(10024, 'Johnsons Baby Soap (125g pack of 3)', 25, 180.00, 150.00, 12, '2024-01-04 14:14:00', 25), "
                 "(10025, 'Patanjali Aloe Vera Juice (500ml)', 37, 120.00, 105.00, 5, '2024-01-04 14:31:00', 37), "
                 "(10026, 'Real Fruit Juice (1L Tetra Pack)', 23, 80.00, 72.00, 5, '2024-01-04 14:36:00', 23), "
                 "(10027, 'Haldiram Moong Dal (500g)', 35, 100.00, 92.00, 5, '2024-01-04 16:22:00', 35), "
                 "(10028, 'Fortune Sunflower Oil (500ml)', 39, 180.00, 162.00, 5, '2024-01-04 16:27:00', 39), "
                 "(10029, 'Parachute Coconut Hair Oil (200ml)', 46, 180.00, 142.00, 18, '2024-01-04 18:16:00', 46), "
                 "(10030, 'Haldiram Soan Papdi (250g tin)', 50, 280.00, 230.00, 12, '2024-01-04 20:13:00', 50), "
                 "(10031, 'Amul Fresh Cream (200ml)', 58, 150.00, 135.00, 5, '2024-01-05 07:54:00', 58), "
                 "(10032, 'MTR Sambhar Powder (200g)', 31, 75.00, 68.00, 5, '2024-01-05 09:15:00', 31), "
                 "(10033, 'Kelloggs Corn Flakes (500g)', 56, 200.00, 168.00, 5, '2024-01-05 11:24:00', 56), "
                 "(10034, 'Kissan Strawberry Jam (500g)', 22, 80.00, 72.00, 5, '2024-01-05 13:19:00', 22), "
                 "(10035, 'Hit Mosquito Killer (150ml)', 32, 80.00, 64.00, 18, '2024-01-05 15:52:00', 32), "
                 "(10036, 'Lifebuoy Total Immunity Soap (125g pack of 3)', 33, 70.00, 65.00, 0, '2024-01-05 19:05:00', 33), "
                 "(10037, 'Aashirvaad Basmati Rice (5kg)', 27, 450.00, 400.00, 5, '2024-01-06 09:14:00', 27), "
                 "(10038, 'Fortune Sunflower Oil (1L)', 42, 160.00, 132.00, 5, '2024-01-06 12:08:00', 42), "
                 "(10039, 'Britannia Good Day Biscuits (100g pack of 2)', 58, 90.00, 72.00, 18, '2024-01-06 12:47:00', 58), "
                 "(10040, 'Pears Soap (125g pack of 3)', 26, 150.00, 130.00, 0, '2024-01-06 14:29:00', 26), "
                 "(10041, 'Fortune Organic Basmati Rice (1kg)', 40, 300.00, 260.00, 5, '2024-01-06 16:12:00', 40), "
                 "(10042, 'Surf Excel Detergent Bar (750g)', 24, 100.00, 74.00, 28, '2024-01-06 16:41:00', 24), "
                 "(10043, 'Maggi Hot & Sweet Sauce (250ml)', 49, 100.00, 92.00, 5, '2024-01-06 18:02:00', 49), "
                 "(10044, 'Red Label Tea 500g', 38, 320.00, 280.00, 5, '2024-01-06 18:23:00', 38), "
                 "(10045, 'Fortune Atta (10kg)', 45, 400.00, 350.00, 5, '2024-01-06 20:38:00', 45), "
                 "(10046, 'Fortune Sunflower Oil Pouch (2L)', 48, 300.00, 260.00, 5, '2024-01-07 07:25:00', 48), "
                 "(10047, 'Patanjali Cow Ghee (500ml)', 40, 380.00, 340.00, 5, '2024-01-07 07:46:00', 40), "
                 "(10048, 'Britannia Good Day Butter Cookies (200g)', 59, 150.00, 140.00, 0, '2024-01-07 09:07:00', 59), "
                 "(10049, 'MTR Gulab Jamun Mix', 20, 85.00, 74.00, 18, '2024-01-07 10:11:00', 20), "
                 "(10050, 'Parle-G Biscuits (500g)', 54, 75.00, 62.00, 0, '2024-01-07 13:32:00', 54), "
                 "(10051, 'Saffola Active Refined Oil (500ml)', 47, 300.00, 270.00, 5, '2024-01-07 15:09:00', 47), "
                 "(10052, 'Haldiram Aloo Bhujia 250g', 18, 65.00, 52.00, 18, '2024-01-07 16:37:00', 18), "
                 "(10053, 'Britannia Marie Gold Biscuits (750g)', 56, 150.00, 142.00, 0, '2024-01-07 17:18:00', 56), "
                 "(10054, 'Britannia Marie Gold Biscuits (400g)', 43, 70.00, 66.00, 0, '2024-01-07 17:21:00', 43), "
                 "(10055, 'Himalaya Green Tea (100g pack of 25)', 38, 200.00, 180.00, 5, '2024-01-07 19:16:00', 38), "
                 "(10056, 'Amul Butter (500g)', 34, 300.00, 265.00, 5, '2024-01-07 20:30:00', 34), "
                 "(10057, 'Saffola Active Refined Oil 1L', 10, 275.00, 250.00, 5, '2024-01-08 10:02:00', 10), "
                 "(10058, 'Maggi Masala Noodles 12-pack', 40, 360.00, 285.00, 18, '2024-01-08 11:18:00', 40), "
                 "(10059, 'Dabur Red Toothpaste 200g', 55, 110.00, 88.00, 18, '2024-01-08 12:05:00', 55), "
                 "(10060, 'Sunfeast Yippee Noodles (80g pack of 5)', 36, 70.00, 58.00, 12, '2024-01-08 13:42:00', 36), "
                 "(10061, 'Ariel Detergent Powder 1kg', 32, 220.00, 175.00, 18, '2024-01-08 14:45:00', 32), "
                 "(10062, 'Kelloggs Chocos (375g)', 48, 180.00, 152.00, 12, '2024-01-08 15:01:00', 48), "
                 "(10063, 'Aashirvaad Atta 5kg', 45, 285.00, 240.00, 5, '2024-01-08 15:32:00', 45), "
                 "(10064, 'MTR Instant Upma (200g)', 42, 95.00, 86.00, 5, '2024-02-02 18:23:00', 42)")