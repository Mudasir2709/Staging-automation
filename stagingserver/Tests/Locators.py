from selenium.webdriver.common.by import By


class class_Locators:

    "Locator for hamburger menu"
    hamburger_menu = (By.XPATH,"//*[@id='html']/body/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/img")

    """Locators for my video page """
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

    """Admin side locators """
    admin_user_name = (By.XPATH,"//input[@name='email']")
    admin_pass = (By.XPATH,"//input[@id='password']")
    admin_submit = (By.XPATH,"//span[text()='Login']")
    videos_tab = (By.XPATH,"//p[text()='Videos']")
    created_video = (By.XPATH,"//p[@title='remove']")
    approve_button = (By.CSS_SELECTOR,r"body > div:nth-child(8) > div > section.block.md\:block.w-full.h-full.md\:w-4\5 > div.pb-2 > div:nth-child(1) > div.h-20 > section > div.w-3\/12.flex.items-center.justify-end > div > div > button")

    """Product tab navigation"""
    product_tab = (By.XPATH,"//p[text()='Access & Security']")

    """New wish list locators """
    new_folder = (By.XPATH, "//h4[text()='+ New Folder']")
    folder_name = (By.XPATH, "//input[@id='Name*']")
    folder_submit_button = (By.XPATH,"//span[text()='Submit']")

    wish_list = (By.CSS_SELECTOR, r"#oJZ0qp0mNcqfoRNQJt5qxA\=\= > div > div.relative.aspect-\[4\/3\].rounded-md.border.border-bw-typo-50.shadow-400.imageHolder.bottom-0.transition-all > div > div > div.cursor-pointer.z-30 > svg > path")
    created_list = (By.XPATH, "//span[text()='Construction designs']")

    """Building world logo locators """
    building_world = (By.XPATH, "(//p[text()='BuildingWorld'])[1]")

    idea_section = (By.XPATH, "(//p[text()='Residential'])[1]")

    idea_wishlist1 = (By.CSS_SELECTOR, r"#dNHF9TZ8gs0dvxiwHDZDtg\=\= > div > div.relative.animate__animated.animate__fadeIn.cursor-pointer > div > div.flex.flex-col.gap-2.relative > div > div > div > div > div.cursor-pointer.z-30 > svg > path")
    navigating_service = (By.XPATH,"//p[text()='Architect & Building Consultant']")
    service_wishlist = (By.CSS_SELECTOR,r"body > div:nth-child(19) > div.lg\:mx-\[100px\].xl\:mx-20.lg\:mt-\[10px\].flex.gap-10.mb-5 > div.w-full.lg\:w-\[40\%\] > div.m-4.lg\:my-4.lg\:mx-0.relative > div > div:nth-child(1) > div > div > div.w-full.relative.lg\:pr-10.pr-5 > div.absolute.top-0.right-0 > div > div.cursor-pointer.z-30 > svg > path")
    sort_by = (By.XPATH,"//p[text()='Latest']")
    my_wish_list_page = (By.XPATH,"(//p[text()='My Wishlist'])[1]")
    created_folder = (By.XPATH,"//span[text()='Construction designs']")

    """My project locators"""
    my_project_button = (By.XPATH, "(//p[text()=' My Projects'])[1]")
    add_project = (By.XPATH,"//span[text()='Add Project']")
    project_upload_button = (By.XPATH,"(//span[text()='Browse'])[1]")
    project_done = (By.XPATH,"//span[text()='Done']")
    project_name = (By.XPATH,"//input[@id='ProjectName*']")
    types_of_building_click = (By.XPATH,"(//div[@class=' css-1wy0on6'])[1]")
    types_of_buildings_suggestion = (By.XPATH,"//p[text()='Commercial']")
    project_location = (By.XPATH,"//*[@id='html']/body/main/div/div[5]/div[2]/div/div[6]/div[1]/div/div/div/input")
    project_location_suggestion = (By.XPATH,"//div[text()='Salem, Tamil Nadu']")
    project_submit_button = (By.XPATH,"//button[normalize-space()='Submit']")

    """Profile icon locator"""
    profile_icon = (By.XPATH,"(//img[@class='rounded-[100px] max-w-none w-[36px] h-[36px] object-cover'])[1]")

    """Sign up Locator"""
    sign_up = (By.XPATH,"(//p[text()='Sign Up'])[2]")

    """Sign up locators"""
    sign_up_email_field = (By.XPATH,"//input[@id='Phone Number or Email']")
    get_otp = (By.XPATH, "//span[text()='Get OTP']")
    otp_1 = (By.XPATH, "//input[@aria-label='Please enter OTP character 1']")
    otp_2 = (By.XPATH, "//input[@aria-label='Please enter OTP character 2']")
    otp_3 = (By.XPATH,"//input[@aria-label='Please enter OTP character 3']")
    otp_4 = (By.XPATH,"//input[@aria-label='Please enter OTP character 4']")
    verify_button = (By.XPATH,"//span[text()='Verify']")
    password_1 = (By.XPATH, "//input[@id='Create']")
    password_2 = (By.XPATH, "//input[@id='Confirm']")
    continue_button = (By.XPATH, "//span[text()='Continue']")

    """User selection locator """
    user_selection = (By.XPATH,"//div[text()='User']")

    """End user locator """
    user_name = (By.XPATH,"//input[@id='Name*']")
    user_phone_number = (By.XPATH, "//input[@id='Phone number**']")
    phone_number_verify = (By.XPATH,"//p[text()='Verify']")
    user_location = (By.XPATH,'//*[@id="html"]/body/main/div/div[6]/div/div[6]/div/div/div/div/input')
    user_location_dropdown = (By.XPATH, "//div[text()='Salem, Tamil Nadu']")
    check_box = (By.XPATH,"//input[@id='terms']")
    password_verify_submit = (By.XPATH,"(//span[text()='Submit'])[2]")
    user_submit = (By.XPATH,"//span[text()='Submit']")

    """Dealer user locator"""
    user_selection2 = (By.XPATH, "//div[text()='Dealer / Store']")
    dealer_address = (By.XPATH,"//*[@id='Address']")
    dealer_location_served = (By.XPATH, '//*[@id="html"]/body/main/div/div[6]/div/div[6]/div[2]/div/div/div/span/div/div/input')
    dealer_location_served_suggestion = (By.XPATH,"//label[@for='Salem, Tamil Nadu']")
    document_type_dropdown = (By.XPATH,"//div[text()='Select...']")
    document_type_select = (By.XPATH,"//p[@title='GST']")
    dealer_id_number = (By.XPATH, "//input[@id='idNumber']")
    document_verify_submit = (By.XPATH,"(//span[text()='Submit'])[2]")
    dealer_browse = (By.XPATH,"(//span[text()='Browse'])[2]")
    dealer_submit = (By.XPATH,"//*[@id='html']/body/main/div/div[6]/div/div[12]/button")

    """Service account locators"""
    user_selection3 = (By.XPATH,"//div[text()='Service']")
    service_phone_number = (By.XPATH,"//input[@id='Phone Number**']")
    service_phone_number_verify = (By.XPATH, "(//p[text()='Verify'])[1]")
    service_phone_number_submit = (By.XPATH,"//span[text()='Submit']")
    service_city = (By.XPATH,"//*[@id='html']/body/main/div/div[6]/div/div[11]/div[2]/div/div/div/input")
    service_city_suggestion = (By.XPATH, "//div[text()='Salem, Tamil Nadu']")
    service_document_type = (By.XPATH, "//p[text()='GST']")
    service_id_number = (By.XPATH,"//input[@id='ID Number']")
    service_id_verify =(By.XPATH, "(//p[text()='Verify'])[1]")
    service_document_verify_submit = (By.XPATH,"(//span[text()='Submit'])")
    service_document_browse = (By.XPATH,"(//span[text()='Browse'])[3]")
    service_continue = (By.XPATH,"//span[text()='Continue']")
    service_types_of_service = (By.CSS_SELECTOR,"body > main > div > div.container.px-4.lg\:px-9.lg\:max-w-5xl.mx-auto.shadow-400.lg\:mt-0.lg\:mb-20.lg\:rounded-xl.min-h-screen > div > div:nth-child(3) > div:nth-child(2) > div > div > div > div > img")
    service_type_of_service_suggestion = (By.XPATH,"//span[text()='Civil Engineers']")
    service_specialization = (By.XPATH, '//*[@id="html"]/body/main/div/div[6]/div/div[3]/div[3]/div/div/div/div')
    service_specialization_suggestion = (By.XPATH,"//span[text()='Commercial']")
    service_location_served = (By.XPATH,'//*[@id="html"]/body/main/div/div[6]/div/div[3]/div[5]/div/div/div/span/div/div/input')
    service_location_served_suggestion = (By.XPATH,"//label[text()='Salem, Tamil Nadu']")
    service_document_select = (By.XPATH, "//div[text()='--Select--']")








