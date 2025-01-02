from selenium.webdriver.common.by import By


class class_Locators:

    "Locator for hamburger menu"

    hamburger_menu = (By.XPATH,"//*[@id='html']/body/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/img")
    my_videos = (By.XPATH,"(//p[text()='My Videos'])[1]")
    create_video = (By.CSS_SELECTOR,"button[class='py-3 px-4 hidden rounded-full w-full lg:flex gap-2 items-center text-sm font-semibold opacity-100 bg-bw-blue-500 text-white hover:bg-bw-blue-500']")
    browse_button = (By.XPATH,"//span[text()='Browse']")
    video_name = (By.XPATH,"//input[@name= 'title']")
    description_field = (By.XPATH,"//textarea[@name='description']")
    location_field = (By.XPATH,"(//input[@type='text'])[2]")
    location_dropdown = (By.XPATH,"//div[text()='Salem, Tamil Nadu']")
    tags_field = (By.XPATH,"//input[@name='tags']")
    tags_suggestion = (By.XPATH,"//li[text()='fencing product']")
    submit_button = (By.XPATH,"//span[text()='Submit']")
    admin_user_name = (By.XPATH,"//input[@name='email']")
    admin_pass = (By.XPATH,"//input[@id='password']")
    admin_submit = (By.XPATH,"//span[text()='Login']")
    videos_tab = (By.XPATH,"//p[text()='Videos']")
    created_video = (By.XPATH,"//p[@title='remove']")
    approve_button = (By.CSS_SELECTOR,r"body > div:nth-child(8) > div > section.block.md\:block.w-full.h-full.md\:w-4\5 > div.pb-2 > div:nth-child(1) > div.h-20 > section > div.w-3\/12.flex.items-center.justify-end > div > div > button")
    product_tab = (By.XPATH,"//p[text()='Access & Security']")
    new_folder = (By.XPATH, "//h4[text()='+ New Folder']")
    folder_name = (By.XPATH, "//input[@id='Name*']")
    folder_submit_button = (By.XPATH,"//span[text()='Submit']")
    wish_list = (By.CSS_SELECTOR, r"#oJZ0qp0mNcqfoRNQJt5qxA\=\= > div > div.relative.aspect-\[4\/3\].rounded-md.border.border-bw-typo-50.shadow-400.imageHolder.bottom-0.transition-all > div > div > div.cursor-pointer.z-30 > svg > path")
    created_list = (By.XPATH, "//span[text()='Construction designs']")
    building_world = (By.XPATH, "(//p[text()='BuildingWorld'])[1]")
    idea_section = (By.XPATH, "(//p[text()='Residential'])[1]")
    idea_wishlist1 = (By.CSS_SELECTOR, r"#dNHF9TZ8gs0dvxiwHDZDtg\=\= > div > div.relative.animate__animated.animate__fadeIn.cursor-pointer > div > div.flex.flex-col.gap-2.relative > div > div > div > div > div.cursor-pointer.z-30 > svg > path")
    navigating_service = (By.XPATH,"//p[text()='Architect & Building Consultant']")
    service_wishlist = (By.CSS_SELECTOR,r"body > div:nth-child(19) > div.lg\:mx-\[100px\].xl\:mx-20.lg\:mt-\[10px\].flex.gap-10.mb-5 > div.w-full.lg\:w-\[40\%\] > div.m-4.lg\:my-4.lg\:mx-0.relative > div > div:nth-child(1) > div > div > div.w-full.relative.lg\:pr-10.pr-5 > div.absolute.top-0.right-0 > div > div.cursor-pointer.z-30 > svg > path")
    sort_by = (By.XPATH,"//p[text()='Latest']")
    my_wish_list_page = (By.XPATH,"(//p[text()='My Wishlist'])[1]")
    created_folder = (By.XPATH,"//span[text()='Construction designs']")
