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
    approve_button = (By.CSS_SELECTOR,"body > div:nth-child(8) > div > section.block.md\:block.w-full.h-full.md\:w-4\/5 > div.pb-2 > div:nth-child(1) > div.h-20 > section > div.w-3\/12.flex.items-center.justify-end > div > div > button")
