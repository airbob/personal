#iOS notes

### how to implement async calls 
```objective-c
- (void)viewDidLoad
{
    [super viewDidLoad];
 
    dispatch_async(kBgQueue, ^{
        NSData* data = [NSData dataWithContentsOfURL: 
          kLatestKivaLoansURL];
        [self performSelectorOnMainThread:@selector(fetchedData:) 
          withObject:data waitUntilDone:YES];
    });
}
- (void)fetchedData:(NSData *)responseData {
    //parse out the json data
    NSError* error;
    NSDictionary* json = [NSJSONSerialization 
        JSONObjectWithData:responseData //1
 
        options:kNilOptions 
        error:&error];
 
    NSArray* latestLoans = [json objectForKey:@"loans"]; //2
    // 1) Get the latest loan
    NSDictionary* loan = [latestLoans objectAtIndex:0];
     
    // 2) Get the funded amount and loan amount
    NSNumber* fundedAmount = [loan objectForKey:@"funded_amount"];
    NSNumber* loanAmount = [loan objectForKey:@"loan_amount"];
    float outstandingAmount = [loanAmount floatValue] - [fundedAmount floatValue];
     
    // 3) Set the label appropriately
    humanReadble.text = [NSString stringWithFormat:@"Latest loan: %@ 
      from %@ needs another $%.2f to pursue their entrepreneural dream",
      [loan objectForKey:@"name"],
      [(NSDictionary*)[loan objectForKey:@"location"] 
        objectForKey:@"country"],
        outstandingAmount];
}
```

[Reference](http://www.raywenderlich.com/5492)


### where set table view cell separators:
tableview-> attribule inspector -> separator -> single line

### change separator line color: 
```objective-c
self.tableView.separatorColor = [UIColor whiteColor];
```

### objecitve-c syntax related:
+: class method <br>
-: instance method <br>
filename+filename.h/m: That is the convention for naming files, that contain categories for existing classes. Categories are a way of adding methods to an existing class in Objective-C, without subclassing

###how to change tableview background color
```objective-c
[self.tableView setBackgroundColor:[UIColor yellowColor]];
```

### how to change tableview background image
```objective-c
    self.tableView.backgroundView = [[UIImageView alloc] initWithImage:[UIImage imageNamed:@"table_background.png"]];
```

### customize section head of table view
```objective-c
-(UIView *) tableView:(UITableView *)tableView viewForHeaderInSection:(NSInteger)section {
    static NSString *CellIdentifier = @"SectionHeader";
    UITableViewCell *headerView = [tableView dequeueReusableCellWithIdentifier:CellIdentifier];
    if (headerView == nil){
        [NSException raise:@"headerView == nil.." format:@"No cells with matching CellIdentifier loaded from your storyboard"];
    }
    return headerView;
}
```
### height of section head of table view 
```objective-c
- (CGFloat)tableView:(UITableView *)tableView heightForHeaderInSection:(NSInteger)section
    {
        return 40.0;
    }
```
### how to convert uicolor with hex color
[reference](http://uicolor.org/)
I note previous reference link will not work properly in 64bit iOS device, so I use following function now:
```objective-c
-(UIColor *)colorFromHex:(NSString *)hex {
    unsigned int c;
    if ([hex characterAtIndex:0] == '#') {
        [[NSScanner scannerWithString:[hex substringFromIndex:1]] scanHexInt:&c];
    } else {
        [[NSScanner scannerWithString:hex] scanHexInt:&c];
    }
    return [UIColor colorWithRed:((c & 0xff0000) >> 16)/255.0
                           green:((c & 0xff00) >> 8)/255.0
                            blue:(c & 0xff)/255.0 alpha:1.0];
}
```
### hide status bar:
```objective-c
- (BOOL)prefersStatusBarHidden {
    return YES;
}
```
### hide navagition
#### To hide Navigation bar :
```objective-c
[self.navigationController setNavigationBarHidden:YES animated:YES];
```
#### To show Navigation bar :
```objective-c
[self.navigationController setNavigationBarHidden:NO animated:YES];
```
### table view cell select and push to another view and pass some parameters
```objective-c
- (void)tableView:(UITableView *)tableView didSelectRowAtIndexPath:(NSIndexPath *)indexPath 
{
     //add code of another view controller
}
```
[Reference](http://stackoverflow.com/questions/11327052/push-to-next-view-by-clicking-on-table-cell-with-using-storyboard)

### how to change tab bar tint color:
```objective-c
//in app delegate  didFinishLaunchingWithOptions add lines such as 
[[UITabBar appearance] setTintColor:[UIColor whiteColor]];
[[UITabBar appearance] setBarTintColor:[UIColor yellowColor]];
[[UITabBar appearance] setSelectedImageTintColor:[UIColor greenColor]];
//tab bar image unselected color
[[UIView appearanceWhenContainedIn:[UITabBar class], nil] setTintColor:[UIColor whiteColor]];
//for the unselect image color, it can only work once, how to solve it
UITabBarItem *item0 = [self.tabBar.items objectAtIndex:0];
item0.image = [[UIImage imageNamed:@"tab1Unselect.png"] imageWithRenderingMode:UIImageRenderingModeAlwaysOriginal];
item0.selectedImage = [UIImage imageNamed:@"tab1Select.png"];
```
### use notification to update view of another view controller 
[reference](http://stackoverflow.com/questions/14852469/how-to-update-uilabel-from-another-viewcontroller)

### how to hide tableviewcell selection arrow
```objective-c
cell.accessoryType = UITableViewCellAccessoryNone;
```
### navigation view controller, go to previous view
```objective-c
[self.navigationController popViewControllerAnimated:TRUE];
```
### direct query of URL string
```objective-c
### url query string:
NSURL *url = [NSURL URLWithString:@"https://blockchain.info/tobtc?currency=USD&value=1"];
    NSString *webData= [NSString stringWithContentsOfURL:url];
    NSLog(@"%@",webData);
```
### add actions for the text field when user typing 
```objective-c
 [_btcField addTarget:self action:@selector(typeBTC:) forControlEvents:UIControlEventEditingChanged];
```
### how to dismiss decimal pad
```objective-c
### dismiss decimal pad:
 UITapGestureRecognizer *tapRecgonizer = [[UITapGestureRecognizer alloc] initWithTarget:self action:@selector(tap:)];
    [self.view addGestureRecognizer:tapRecgonizer];
- (void) tap: (UIGestureRecognizer* ) gr
{
    NSLog(@"YES, YOU JUST TAPPED");
    [self.view endEditing:YES];
}
```
[Reference](http://code-and-coffee.blogspot.sg/2013/01/how-to-dissmis-decimal-pad-keyboard.html?showComment=1384935807857)

### how to implement the normal "swipe left for settings side bar" ?
[Reference](http://www.appcoda.com/ios-programming-sidebar-navigation-menu/)
### simple drop down list:
[Reference](http://www.edumobile.org/iphone/iphone-programming-tutorials/a-simple-drop-down-list-for-iphone/)
### take screenshot on simulator
edit->copy screen -> open preview, cmd+ s to save
### how to customize left/right swipe segue
```objective-c
//in view did load//
{
    UISwipeGestureRecognizer *rightRecognizer = [[UISwipeGestureRecognizer alloc] initWithTarget:self action:@selector(rightSwipeHandle:)];
    rightRecognizer.direction = UISwipeGestureRecognizerDirectionRight;
    [rightRecognizer setNumberOfTouchesRequired:1];
    [self.view addGestureRecognizer:rightRecognizer];
    UISwipeGestureRecognizer *leftRecognizer = [[UISwipeGestureRecognizer alloc] initWithTarget:self action:@selector(leftSwipeHandle:)];
    leftRecognizer.direction = UISwipeGestureRecognizerDirectionLeft;
    [leftRecognizer setNumberOfTouchesRequired:1];
    [self.view addGestureRecognizer:leftRecognizer];
    }

    - (void)rightSwipeHandle:(UISwipeGestureRecognizer*)gestureRecognizer
{
    [self.navigationController popViewControllerAnimated:YES];
}

- (void)leftSwipeHandle:(UISwipeGestureRecognizer*)gestureRecognizer
{
    [self performSegueWithIdentifier:@"forward" sender:self];
}
```
### how to zoom in/out emulator size?
cmd + 1/2/3
### calling a method for every 60 seconds
```objective-c
- (void)viewDidLoad
{
    [super viewDidLoad];
	// Do any additional setup after loading the view, typically from a nib.
    [NSTimer scheduledTimerWithTimeInterval:60.0
                                     target:self
                                   selector:@selector(someMethod)
                                   userInfo:nil
                                    repeats:YES];
}

- (void) someMethod {
    NSLog(@"hello I am called");
}
```
### how to set view layout compatible for both 3.5inch and 4inch screen
1. auto-layout
2. constrains

### how to distribute your app wirelessly for beta user
main idea: create a new distribute license with allowed iphone udid inside it, compile the code and siging with the license. 
[Reference](http://help.apple.com/iosdeployment-apps/mac/1.1/#app43ad871e)

### how to dismiss alert view after 5 seconds if user did not click "OK"
```objective-c
//method1
[self performSelector:@selector(hideAlertView:) withObject:staticalertView afterDelay:5]
//method2
dispatch_async(dispatch_get_main_queue(), ^{
        [self performSelector:@selector(hideAlertView:) withObject:staticalertView afterDelay:5];
    });
```

### add ios button dynamically and associated them with ibactions:
```objective-c
UIButton *myButton = [[UIButton alloc] init...];
[myButton addTarget:something action:@selector(myAction) forControlEvents:UIControlEventTouchUpInside];
```
[Reference](http://stackoverflow.com/questions/2370031/programatically-generating-uibuttons-and-associate-those-with-ibaction)

### change project name in Xcode, but its name just does not change
Please search for whole project of CFBundleDisplayName, maybe it is hardcoded somewhere.

### when add segue for modal view -> navigation controller view, the navigation bar disappears.
Please connect segue from modal view to navigation controller, not the navigation controller root view


### why UILabel change frame can not work
Plese make sure disable auto-layout 
```objective-c
CGSize maxSize = CGSizeMake(_mainLabel.frame.size.width, MAXFLOAT);
NSString * testString = @"here adlk dal faskdfjl jasdlfjslkadflksadfkl jsakdfsadf dsfdsf asdfasdf asdfasdfasdf asdfasdf sadf sadf ";
CGRect labelRect = [testString boundingRectWithSize:maxSize options:NSStringDrawingUsesLineFragmentOrigin attributes:@{NSFontAttributeName:_mainLabel.font} context:nil];
CGRect frame = _mainLabel.frame;
frame.size.height = labelRect.size.height;
```
### how to access uibutton in uitableviewcell
set uibutton with tag
```objective-c
UIButton *button2 = (UIButton *)[[cell contentView] viewWithTag:2];
```

### how to parse json data without knowing theire keys? 
```objective-c
    NSString *prefix=@"http://ec2-54-251-248-32.ap-southeast-1.compute.amazonaws.com/backup/db/samquery1.php?userid=";
    NSInteger uid = 100;     //let's say user id is 111
    NSString *postfix = [NSString stringWithFormat:@"%ld", (long)uid];
    NSString *qstring = [ prefix stringByAppendingString:postfix];
    NSURL *url=[NSURL URLWithString:qstring];
    NSData *data=[NSData dataWithContentsOfURL:url];
    
    NSError *error=nil;
    NSArray *jsonArray =[NSJSONSerialization JSONObjectWithData:data options:
                         NSJSONReadingMutableContainers error:&error];
    if (!jsonArray) {
        NSLog(@"Error parsing JSON: %@", error);
    } else {
        for(NSDictionary *item in jsonArray) {
            //NSLog(@"Item: %@", item);
            //NSString *negemo = [item objectForKey:@"negemo"];
            //NSLog(@"negative emo is %@", negemo);
            
            NSLog(@"=====start of row=====\n");
            NSArray *keys = [item allKeys];
            for (id key in keys)
            {
                id aValue = [item objectForKey:key];
                NSLog(@"key is %@ and value is %@",key,aValue);
            }
            NSLog(@"=====end of row=====\n");
        }
    }
```

### how to change tableview cell alpha value:
```objective-c
cell.contentView.alpha = 0.5;
```
### how to add different separator for dif tableview cells
in viewdidload add:
```objective-c
self.tableView.separatorColor = [UIColor clearColor];
```
in cellForRowAtIndexPath add
```objective-c
CALayer *separator = [CALayer layer];
        separator.backgroundColor = [UIColor whiteColor].CGColor;
        separator.frame = CGRectMake(0, -1, self.view.frame.size.width, 1);
        [cell.layer addSublayer:separator];
```
### how to write to *.plist file
```objective-c
- (NSApplicationTerminateReply)applicationShouldTerminate:(NSApplication *)sender {
    NSString *error;
    NSString *rootPath = [NSSearchPathForDirectoriesInDomains(NSDocumentDirectory, NSUserDomainMask, YES) objectAtIndex:0];
    NSString *plistPath = [rootPath stringByAppendingPathComponent:@"Data.plist"];
    NSDictionary *plistDict = [NSDictionary dictionaryWithObjects:
            [NSArray arrayWithObjects: personName, phoneNumbers, nil]
            forKeys:[NSArray arrayWithObjects: @"Name", @"Phones", nil]];
    NSData *plistData = [NSPropertyListSerialization dataFromPropertyList:plistDict
                            format:NSPropertyListXMLFormat_v1_0
                            errorDescription:&error];
    if(plistData) {
        [plistData writeToFile:plistPath atomically:YES];
    }
    else {
        NSLog(error);
        [error release];
    }
    return NSTerminateNow;
}
```

### how to change navigation bar tint color
```objective-c
self.navigationController.navigationBar.barTintColor = [UIColor colorWithRed:26/255.0f green:188/255.0f blue:156/255.0f alpha:1.0f];
    self.navigationController.navigationBar.tintColor = [UIColor whiteColor];
    [self.navigationController.navigationBar setTitleTextAttributes:@{NSForegroundColorAttributeName : [UIColor whiteColor]}];
    self.navigationController.navigationBar.translucent = NO;
```
### particular cell is not selectable
```objective-c
    if (indexPath.row == 0)
    {
        // we decide here that first cell in the table is not selectable (it's just an indicator)
        cell.selectionStyle = UITableViewCellSelectionStyleNone;
    }
```
### how to delete a *.plist file programmingly
```objective-c
if(![[NSFileManager defaultManager] removeItemAtPath:documentPlistPath error:&error])
    {
        //TODO: Handle/Log error
        NSLog(@"got error");
    }
    else {
        NSLog(@"delete successfuly");
    }
```
### how to copy bundle plist(which is read only) to document plist file(which is writable)?
```objective-c
NSFileManager *fileManager = [NSFileManager defaultManager];
    NSError *error;
    NSArray *documentPaths = NSSearchPathForDirectoriesInDomains(NSDocumentDirectory, NSUserDomainMask, YES);
    NSString *documentsDirectory = [documentPaths objectAtIndex:0];
    NSString *documentPlistPath = [documentsDirectory stringByAppendingPathComponent:@"messages.plist"];
    NSString *bundlePath = [[NSBundle mainBundle] bundlePath];
    NSString *bundlePlistPath = [bundlePath stringByAppendingPathComponent:@"messages.plist"];
    
    BOOL success = [fileManager copyItemAtPath:bundlePlistPath toPath:documentPlistPath error:&error];
    if (success) {
        NSArray *array = [NSArray arrayWithContentsOfFile:documentPlistPath];
        NSLog(@"success: after copied the plist file is %@", array);
    }
    else {
        NSArray *array = [NSArray arrayWithContentsOfFile:documentPlistPath];
        NSLog(@"fail: after copied the plist file is %@", array);
    }
```

### how to implement iOS7 back swipe gesture?
[reference](http://stackoverflow.com/questions/23321332/how-to-create-custom-back-swipe-gesture-in-uinavigationcontroller-on-ios-7)

### select tableview cell and perform segue with some parameters:
```objective-c
- (void)tableView:(UITableView *)tableView didSelectRowAtIndexPath:(NSIndexPath *)indexPath
{
	[self performSegueWithIdentifier:@"editEvent" sender:[self.tableView cellForRowAtIndexPath:indexPath]];
}
- (void)prepareForSegue:(UIStoryboardSegue *)segue sender:(id)sender
{
    UITableViewCell *cell = sender;
    // Make sure your segue name in storyboard is the same as this line
    NSLog(@"inside prepare for segue");
    if ([[segue identifier] isEqualToString:@"editEvent"])
    {
        //((BTCSegue *)segue).animationType = 0 ;
        // Get reference to the destination view controller
        llEditLogViewController *editViewController = [segue destinationViewController];
        NSIndexPath *indexPath = [self.tableView indexPathForCell:cell];
        NSInteger rowSelected = [indexPath row];
        editViewController.rowSelected = rowSelected;
        NSLog(@"prepare for segue, and row is %ld",(long)rowSelected);
    }
}

### how to parse standard time string and format it (eg: 2014-01-02 10:10:10)?
```objective-c
formatter.dateFormat = @"yyyy-MM-dd HH:mm:ss";
formatter.timeZone = [NSTimeZone timeZoneWithAbbreviation:@"UTC"];
NSDate *date = [formatter dateFromString:[tmpDict objectForKey:@"posttime"]];
NSDateFormatter *formatter2 = [[NSDateFormatter alloc] init];
formatter2.dateFormat = @"dd-MMM HH:mm";
NSString *postTime = [formatter2 stringFromDate:date];
NSLog(@" post time is %@", postTime);
```

### how to add activityIndicator during webview loading?
```objective-c
- (void)viewDidLoad
{
    [super viewDidLoad];
    NSString * urlString = @"......";
    [_postWebView loadRequest:[NSURLRequest requestWithURL:[NSURL URLWithString:urlString]]];
    _postWebView.delegate = self;
}

- (void)webViewDidStartLoad:(UIWebView *)webView{
    [self.postProgress setHidden:NO];
    [self.postProgress startAnimating];
    
}

- (void)webViewDidFinishLoad:(UIWebView *)webView{
    [self.postProgress stopAnimating];
    [self.postProgress setHidden:YES];
}
```

### how to rename delete table view cell "Delete"?
```objective-c
//let's say we want to rename it to close
- (NSString *)tableView:(UITableView *)tableView titleForDeleteConfirmationButtonForRowAtIndexPath:(NSIndexPath *)indexPath {
    return @"Close";
}
```

### iOS push notification implementation
[reference1](http://blog.csdn.net/daydreamingboy/article/details/7977098)
[reference2](http://www.raywenderlich.com/32960/apple-push-notification-services-in-ios-6-tutorial-part-1)


### how to add app walkthrough? 
1. detect whether the user is first time launching app or not [Reference](http://stackoverflow.com/a/13335636/874585)
2. perform segue to walkthrough view if it is first time user [Refenrence](http://www.appcoda.com/uipageviewcontroller-storyboard-tutorial/)

### get URL source code:
```objective-c
NSURL *mobileurl = [NSURL URLWithString:@"http://campusbus.ntu.edu.sg/ntubus/index.php/m/main"];
    NSError* error = nil;
    NSString* text = [NSString stringWithContentsOfURL:mobileurl encoding:NSASCIIStringEncoding error:&error];
    if( text )
    {
        NSLog(@"Text=%@", text);
    }
    else
    {
        NSLog(@"Error = %@", error);
    }
```

### Delete the extra separator of UITableView in iOS 7

```objective-c
- (UIView *)tableView:(UITableView *)tableView viewForFooterInSection:(NSInteger)section
{        
    return [UIView new];
    // If you are not using ARC:
    // return [[UIView new] autorelease];
}
```

### how to add side bar to the view
[reference](http://www.appcoda.com/ios-programming-sidebar-navigation-menu/)

problem: swipe to delete tableview cell seems not working any more.
https://github.com/John-Lluch/SWRevealViewController/issues/104

### long press to re-ordering tableview cells
[reference](https://github.com/bvogelzang/BVReorderTableView)

### how to add line to UIView?
```objective-c
UIView * separator = [[UIView alloc] initWithFrame:CGRectMake(20, 104, 320, (1.0 / [UIScreen mainScreen].scale) / 2)];
    separator.backgroundColor = [UIColor colorWithWhite:0.7 alpha:1];
    [self.view addSubview:separator];
```
#### how to make the line exactly 1px for both normal iOS device as well as retina display device?
```objective-c
CGFloat scaleOfMainScreen = [UIScreen mainScreen].scale;
    CGFloat alwaysOnePixelInPointUnits = 1.0/scaleOfMainScreen;
    
    UIView * separator = [[UIView alloc] initWithFrame:CGRectMake(20, 40, 300, alwaysOnePixelInPointUnits)];
    separator.backgroundColor = [UIColor colorWithWhite:1 alpha:0.2];
    [self.view addSubview:separator];
```    
### dismiss keyboard when user taps other area:
```objective-c
- (void)touchesBegan:(NSSet *)touches withEvent:(UIEvent *)event {
    for (UIView * txt in self.view.subviews){
        if ([txt isKindOfClass:[UITextField class]] && [txt isFirstResponder]) {
            [txt resignFirstResponder];
        }
    }
}

/*OR*/

- (void)touchesBegan:(NSSet *)touches withEvent:(UIEvent *)event {
    [self.view endEditing:YES];    
}
```
[reference](http://stackoverflow.com/questions/18756196/how-to-dismiss-keyboard-when-user-tap-other-area-outside-textfield)

### textfield werid behavior
[ref](http://stackoverflow.com/questions/14252470/how-to-dismiss-keyboard-on-second-time-selecting-first-textfield)
[ref2](http://stackoverflow.com/questions/10051402/keyboard-not-responding-to-resignfirstresponder)


### how to implement movable/reorder tableview cells?
[ref1](https://github.com/yonat/EditableList)


### NSArray and NSMutableArray
```objective-c
NSArray* arr = [[NSArray alloc]initWithObjects:@"work",@"email",@"dreamon",@"aaa",@"bbb",@"ccc", nil];
NSMutableArray *randomSelection =  [[NSMutableArray alloc]init];
[randomSelection addObject:@"string1"];
```
### NSString and NSMutableString 区别?
```objective-c
//NSString is immutable , it equals to constant NSMutableString
//NSMutableString is mutable

```

### how to implement a dropdown list
[example1](https://github.com/nmattisson/DropdownMenu)
[example2](https://github.com/romaonthego/REMenu)
[example3](https://github.com/BijeshNair/NIDropDown)


### how to set view background image?

```objective-c
self.view.backgroundColor = [UIColor colorWithPatternImage:[UIImage imageNamed:@"randomgrey.png"]];
```

#### how to stretch the image if size not fit?
```objective-c
    UIGraphicsBeginImageContext(self.view.frame.size);
    [[UIImage imageNamed:@"chat_blur_default9"] drawInRect:self.view.bounds];
    UIImage *image = UIGraphicsGetImageFromCurrentImageContext();
    UIGraphicsEndImageContext();
    self.view.backgroundColor = [UIColor colorWithPatternImage:image];
```    

### swipe to delete table view cell?
```objective-c
- (BOOL)tableView:(UITableView *)tableView canEditRowAtIndexPath:(NSIndexPath *)indexPath
{
    // Return YES - we will be able to delete all rows
    return YES;
}

- (void)tableView:(UITableView *)tableView commitEditingStyle:(UITableViewCellEditingStyle)editingStyle forRowAtIndexPath:(NSIndexPath *)indexPath
{
    // Perform the real delete action here. Note: you may need to check editing style
    //   if you do not perform delete only.
    NSLog(@"Deleted row.");
}
```


### how to get iPhone simulator directory?
```
dirPaths = NSSearchPathForDirectoriesInDomains(NSDocumentDirectory, NSUserDomainMask, YES);
    docsDir = dirPaths[0];
    NSLog(@"%@",docsDir);
```    

### how to view sqlite visually on mac?
[try this](https://itunes.apple.com/us/app/sqlite-professional-read-only/id635299994?mt=12)


### how to use sqlite?
(follow this tutorial](http://www.techotopia.com/index.php/An_Example_SQLite_based_iOS_7_Application)


### how to add iOS default share sheet?
```objective-c

    NSString *text = @"hello world";
            NSURL *url = [NSURL URLWithString:@"http://airbob.github.io/lifeNumber"];
            //UIImage *image = [UIImage imageNamed:@"roadfire-icon-square-200"];
            
            UIActivityViewController *controller =
            [[UIActivityViewController alloc]
             initWithActivityItems:@[text, url]
             applicationActivities:nil];
            
            
            controller.excludedActivityTypes = @[UIActivityTypePrint,
                                                 UIActivityTypeCopyToPasteboard,
                                                 UIActivityTypeAssignToContact,
                                                 UIActivityTypeSaveToCameraRoll,
                                                 UIActivityTypeAddToReadingList,
                                                 UIActivityTypeAirDrop];
            [self presentViewController:controller animated:YES completion:nil];
```

### how to generate months array?

```objective-c
NSArray *monthlySymbols = [[[NSDateFormatter alloc] init] shortMonthSymbols];
```

### how to iterate date from one year ago to today?
```objective-c 
    NSDate *now = [NSDate date];
    NSDate *seventyDaysAgo = [now dateByAddingTimeInterval:-356*24*60*60];
    //NSLog(@"70 days ago: %@", seventyDaysAgo);
    
    NSDateFormatter *dateFormatter = [[NSDateFormatter alloc] init];
	[dateFormatter setDateFormat:@"yyyy-MM-dd"];
	//NSString *MyString = [dateFormatter stringFromDate:seventyDaysAgo];
    
    
    
    NSCalendar *calendar = [NSCalendar currentCalendar];
    NSDateComponents *oneDay = [[NSDateComponents alloc] init];
    [oneDay setDay: 1];
    
    for (NSDate* date = seventyDaysAgo; [date compare: now] <= 0;
         date = [calendar dateByAddingComponents: oneDay
                                          toDate: date
                                         options: 0] ) {
             //NSLog( @"%@ in [%@,%@]", date, sevenDaysAgo, now );
             NSLog(@"date is %@", [dateFormatter stringFromDate:date]);
         }
```

### how to remove file in document path
```objective-c
- (void)removeFile:(NSString *)fileName
{
    NSFileManager *fileManager = [NSFileManager defaultManager];
    NSString *documentsPath = [NSSearchPathForDirectoriesInDomains(NSDocumentDirectory, NSUserDomainMask, YES) objectAtIndex:0];
    
    NSString *filePath = [documentsPath stringByAppendingPathComponent:fileName];
    NSError *error;
    BOOL success = [fileManager removeItemAtPath:filePath error:&error];
    if (success) {
        NSLog(@"removed");
    }
    else
    {
        NSLog(@"Could not delete file -:%@ ",[error localizedDescription]);
    }
}
```

### how to set keyboard return action?
Adopt the UITextFieldDelegate method and set yourself as the delegate. Implement textFieldShouldReturn: method like this,
```objective-c
- (BOOL)textFieldShouldReturn:(UITextField *)textField {
    [textField resignFirstResponder];
    return YES;
}
```

### how to add hyperlink to button click?
```objective-c 
-(void) buttonpressed:(UIButton *)sender {
    NSString* launchUrl = @"http://apple.com/";
    [[UIApplication sharedApplication] openURL:[NSURL URLWithString: launchUrl]];
}

```

## sprite kit

### how to add a node with image name

```objective-c
CGPoint location = [touch locationInNode:self];
        
        SKSpriteNode *sprite = [SKSpriteNode spriteNodeWithImageNamed:@"Spaceship"];
        
        sprite.position = location;
        
        SKAction *action = [SKAction rotateByAngle:M_PI duration:1];
        
        [sprite runAction:[SKAction repeatActionForever:action]];
        
        [self addChild:sprite];

```
### how to detect general SKNode touched?
```objective-c
-(void)touchesBegan:(NSSet *)touches withEvent:(UIEvent *)event {
    UITouch *touch = [touches anyObject];
    CGPoint touchLocation = [touch locationInNode:self];
    SKNode *touchedNode = [self nodeAtPoint:touchLocation];
    
    NSLog(@"touchLocation x: %f and y: %f", touchLocation.x, touchLocation.y);
    
    if (touchedNode != self) {
        NSLog(@"Removed from parent.");
        //[touchedNode removeFromParent];
        UIViewController *vc = self.view.window.rootViewController;
        [vc performSegueWithIdentifier:@"toSettings" sender:nil];
    }
}

```

### how to detect certain SKNode touched?

```objective-c
//assign the name property when add the node:
        //      second label
        SKLabelNode *myLabel2 = [SKLabelNode labelNodeWithFontNamed:@"Chalkduster"];
        //        myLabel2.userInteractionEnabled = YES;
        myLabel2.name = @"nodename";
        myLabel2.text = @"Hello, World!";
        myLabel2.fontSize = 30;
        myLabel2.position = CGPointMake(100, 100);
        [self addChild:myLabel2];
        
-(void)touchesBegan:(NSSet *)touches withEvent:(UIEvent *)event {
    UITouch *touch = [touches anyObject];
    CGPoint touchLocation = [touch locationInNode:self];
    SKNode *touchedNode = [self nodeAtPoint:touchLocation];
    
    NSLog(@"touchLocation x: %f and y: %f", touchLocation.x, touchLocation.y);
    
    if ([touchedNode.name isEqualToString:@"nodename"]) {
        NSLog(@"Removed from parent.");
        //[touchedNode removeFromParent];
        UIViewController *vc = self.view.window.rootViewController;
        [vc performSegueWithIdentifier:@"toSettings" sender:nil];
    }
}
```
## iAd
### how to add iAd:
case 1: juse add a normal iAd banner at bottom of view:
step 1: build phase add linked framework (iAds) <br/>
step 2: add ```#import <iAd/iAd.h>``` in *.h file, in *.m viewdidLoad add ``` self.canDisplayBannerAds = YES;```<br>
[Reference](http://www.youtube.com/watch?v=fP2ijcXbCz4)
[Reference2](http://stackoverflow.com/questions/19717446/how-to-have-an-in-app-purchase-to-remove-iads)

case 2: add iAd banner in the view
step1: add framework <br>
step2: import iAd and add ADBannerViewDelegate <br>
step3: add banner to view, drag and link IBOutlet<br>
step4: add following methods:

```objective-c
-(void)bannerView:(ADBannerView *)banner
didFailToReceiveAdWithError:(NSError *)error{
    NSLog(@"Error in Loading Banner!");
}

-(void)bannerViewDidLoadAd:(ADBannerView *)banner{
    NSLog(@"iAd banner Loaded Successfully!");
}
-(void)bannerViewWillLoadAd:(ADBannerView *)banner{
    NSLog(@"iAd Banner will load!");
}
-(void)bannerViewActionDidFinish:(ADBannerView *)banner{
    NSLog(@"iAd Banner did finish");
    
}
```

### how to use blocks?

[ref1](http://rypress.com/tutorials/objective-c/blocks.html)
[ref2](https://developer.apple.com/library/ios/documentation/Cocoa/Conceptual/ProgrammingWithObjectiveC/ProgrammingWithObjectiveC.pdf)
[ref3](http://stackoverflow.com/questions/19171206/save-a-completion-handler-as-an-object)


## game center:
step1: add GameKit framework<br>
step2: import ```#import <GameKit/GameKit.h>``` and add ```GKGameCenterControllerDelegate```
step3: add authenticate function:
```objective-c
#pragma mark - game center functions
[self authenticateLocalPlayer];
-(void)authenticateLocalPlayer{
    GKLocalPlayer *localPlayer = [GKLocalPlayer localPlayer];
    
    localPlayer.authenticateHandler = ^(UIViewController *viewController, NSError *error){
        if (viewController != nil) {
            [self presentViewController:viewController animated:YES completion:nil];
        }
        else{
            if ([GKLocalPlayer localPlayer].authenticated) {
                _gameCenterEnabled = YES;
                
                // Get the default leaderboard identifier.
                [[GKLocalPlayer localPlayer] loadDefaultLeaderboardIdentifierWithCompletionHandler:^(NSString *leaderboardIdentifier, NSError *error) {
                    
                    if (error != nil) {
                        NSLog(@"%@", [error localizedDescription]);
                    }
                    else{
                        _leaderboardIdentifier = leaderboardIdentifier;
                        NSLog(@"leader board identifier name is %@", _leaderboardIdentifier);
                    }
                }];
            }
            
            else{
                _gameCenterEnabled = NO;
            }
        }
    };
}
```
### how to integrate game center in your app?
[Ref1](http://www.appcoda.com/ios-game-kit-framework/)
[Ref2](http://www.raywenderlich.com/3276/game-center-tutorial-for-ios-how-to-make-a-simple-multiplayer-game-part-12)


### how to set navigation bar title with a text field?
```objective-c
    UITextField *textField = [[UITextField alloc]initWithFrame:CGRectMake(0, 0, 200, 22)];
        textField.text = @"Insert Title Here";
    textField.font = [UIFont boldSystemFontOfSize:19];
    textField.textColor = [UIColor whiteColor];
    textField.textAlignment = NSTextAlignmentCenter;
    textField.delegate = self;
    self.navigationItem.titleView = textField;
```

### how to set user default and sync it?
```objective-c
//when set 
[[NSUserDefaults standardUserDefaults] setObject:textField.text forKey:@"mainTitle"];
[[NSUserDefaults standardUserDefaults] synchronize];
//when get
NSString *tempTitle = [[NSUserDefaults standardUserDefaults] objectForKey:@"mainTitle"];
```

### how to detect when hit return of textfield?
step1: add UITextFieldDelegate
step2: add 
```objective-c
-(BOOL) textFieldShouldReturn:(UITextField *)textField{
    NSLog(@"text field is %@", textField.text);
    [textField resignFirstResponder];
    return YES;
}
```

### how to set uibutton round corner?
```objective-c
    self.button.layer.masksToBounds = YES;
    self.button.layer.cornerRadius = 5.0;
```

### how to add border with color for UIButton?
```objective-c
    [[self.button layer] setBorderWidth:2.0f];
    [[self.button layer] setBorderColor:[UIColor whiteColor].CGColor];
```

### how to implement long press gesture to re order the tableview items?
[reference](http://www.raywenderlich.com/63089/cookbook-moving-table-view-cells-with-a-long-press-gesture)

### how to make circular image and add border?
```objective-c
//circle
self.profileImageView.layer.cornerRadius = self.profileImageView.frame.size.width / 2;
self.profileImageView.clipsToBounds = YES;
//border
self.profileImageView.layer.borderWidth = 3.0f;
self.profileImageView.layer.borderColor = [UIColor whiteColor].CGColor;
```

### how to programmingly add event to reminder:
[reference](http://stackoverflow.com/questions/15864595/programatically-add-a-reminder-to-the-reminders-app)

### how to implement local notification
[reference](http://www.appcoda.com/ios-programming-local-notification-tutorial/)

### how to add clickable action for imageview?
```objective-c
UITapGestureRecognizer *singleTap = [[UITapGestureRecognizer alloc] initWithTarget:self action:@selector(tapDetected)];
singleTap.numberOfTapsRequired = 1;
self.imageView.userInteractionEnabled = YES;
[self.imageView addGestureRecognizer:singleTap];
```

### how to dismiss view controller after certain animation (such as modal view, partial curl)
```objective-c
[self dismissViewControllerAnimated:YES completion:nil];
```

### remind the user after some period did not open the app
[reference](http://www.youtube.com/watch?v=fnhIVCz2xJ4)

### NSDate how to get several days ago?
```objective-c
NSDate *now = [NSDate date];
NSDate *sevenDaysAgo = [now dateByAddingTimeInterval:-7*24*60*60];
NSLog(@"7 days ago: %@", sevenDaysAgo);
```

### iCloud tutorials
[ref1](http://www.raywenderlich.com/6015/beginning-icloud-in-ios-5-tutorial-part-1)
[ref2](http://www.raywenderlich.com/6031/beginning-icloud-in-ios-5-tutorial-part-2)
[ref3](http://www.appcoda.com/icloud-programming-ios-intro-tutorial/)

### how to cancel all local push notifications?
```objective-c
UIApplication *app = [UIApplication sharedApplication];
[app cancelAllLocalNotifications];
```

### weak/strong/assign/copy/retain discussion
[reference](http://stackoverflow.com/questions/8927727/objective-c-arc-strong-vs-retain-and-weak-vs-assign(

### use applescript to auto login itunes
[reference](http://computers.tutsplus.com/tutorials/creating-an-applescript-to-switch-between-multiple-itunes-accounts--mac-49681)


### iOS with different URL:
[reference](http://iosdevelopertips.com/cocoa/launching-other-apps-within-an-iphone-application.html)


### how to change UITableViewCellAccessory-DisclosureIndicator colour
```objective-c
//normally replace the arrow with an image

cell.accessoryView = [[UIImageView alloc] initWithImage:[UIImage imageNamed:@"disclosureIndicator.png"]];
```

### how to add uiview programmingly ?
```objective-c
UIView *cv = [[UIView alloc]initWithFrame:CGRectMake(0, self.view.frame.size.height, 320, 216)]; //creat an instance of your custom view
    cv.backgroundColor = [UIColor colorWithRed:0.941 green:0.941 blue:0.941 alpha:1];
    [self.view addSubview:cv]; // add to your main view
```

### how to move view up when keyboard shows up
1. add listener to keyboard show or hide<br>
2. set the center (up keyboard height: 216px) when keyboard shows <br>
3. reset to original center after keyboard hide <br>
[reference](http://stackoverflow.com/questions/16752154/move-uiview-when-keyboard-appears)
[reference](http://stackoverflow.com/questions/15036519/scroll-uitextfield-above-keyboard-in-a-uitableviewcell-on-a-regular-uiviewcontro)

### how to add search bar in tableview
[reference](http://www.appcoda.com/search-bar-tutorial-ios7/)

### how to hide tab bar if needed:
```objective-c
self.tabBarController.tabBar.hidden=YES;
```

### how to add horizontal scrollable view menu?
[ref](http://stackoverflow.com/questions/18069007/how-to-make-horizontal-scrolling-menu-in-ios)


### UISearchResultsTableView dequeueReusableCellWithIdentifier error?
```objectiv-c
// use self.tableview insead of tableview when dequeue with identifier
```

### how to reload data in tableview of a container view?
```objective-c
UITableViewController *tbc = (UITableViewController *)self.childViewControllers[0];
[tbc.tableView reloadData];
```

### how to trigger map view to show callout annotations?
```objective-c
- (void)mapView:(MKMapView *)mapView didAddAnnotationViews:(NSArray *)views
{
    //Here
    [mapView selectAnnotation:[[mapView annotations] lastObject] animated:YES];
}
```

[reference](http://stackoverflow.com/questions/978897/how-to-trigger-mkannotationviews-callout-view-without-touching-the-pin)


### how to implement UILabel auto height in iOS7?
1. not auto-layout case:
```objective-c
self.mainLabel.lineBreakMode = NSLineBreakByWordWrapping;
    self.mainLabel.numberOfLines = 0;
    
    NSString *someText = @"this is a really long long message, this is a really long long message, this is a really long long message, this is a really long long message, this is a really long long message, this is a really long long message, this is a really long long message, this is a really long long message-===== end ";
    //key part: calculate the frame size
    CGSize maxSize = CGSizeMake(320.f, FLT_MAX);
    CGRect labRect = [someText boundingRectWithSize:maxSize options:NSStringDrawingUsesLineFragmentOrigin attributes:@{NSFontAttributeName:self.mainLabel.font} context:nil];
    self.mainLabel.frame = CGRectMake(0, 64, maxSize.width, labRect.size.height);
    self.mainLabel.text = someText;
     
```
2. auto-layout case
```objective-c
//uilabel inspector: line break mode: word wrap
//add constrains to the UILabel, height >= some value
//If you implement UILabel in UItableView, still use boundingRectWithSize to calculate height of UILabel, then calculate the offset accordingly
```
[reference](http://stackoverflow.com/questions/12789013/ios-multi-line-uilabel-in-auto-layout)



### articles
[do not abuse app delegate](http://www.hollance.com/2012/02/dont-abuse-the-app-delegate/)

### long press gesture for image view
[ref](http://stackoverflow.com/questions/17833150/long-press-gesture-and-movement-of-uiimageview)

### how to implement uicollectionview
[ref](http://www.techotopia.com/index.php/An_iOS_7_Storyboard-based_Collection_View_Tutorial)


### for imageview tap gesture, how to reference the sender?
[ref](http://stackoverflow.com/questions/6082244/uitapgesturerecognizer-selector-sender-is-the-gesture-not-the-ui-object)

### how to display and dismiss modal view programmingly?
```objective-c
[self presentViewController:modalViewController animated:YES completion:nil];
[self dismissViewControllerAnimated:YES completion:nil];
```
### when display a modal view programmingly, it displays a balck screen, why?
```objective-c
CBModalViewController* modalViewController = [[CBModalViewController alloc] init]; 
/*this is inconrect if you use storyboard, use following method 
(please note the controller identifier is the storyboard id in storyboard
*/

    UIStoryboard *mainStoryboard = [UIStoryboard storyboardWithName:@"Main"
                                                             bundle: nil];
    
    CBModalViewController * modalViewController = (CBModalViewController*)[mainStoryboard
    instantiateViewControllerWithIdentifier: @"CBModalViewController"];
```

### how to get position of each tab bar?
```
for (UIView* view in self.tabBar.subviews)
    {
        NSLog(@"view descritipon %@", view.description);
    }
```

### how remove the 1px black border under navigation bar?
```
//need to add a subview to overlay it
UIView *navBorder = [[UIView alloc] initWithFrame:CGRectMake(0,navigationBar.frame.size.height-1,navigationBar.frame.size.width, 1)]; 

// Change the frame size to suit yours //

[navBorder setBackgroundColor:[UIColor colorWithWhite:200.0f/255.f alpha:0.8f]];
[navBorder setOpaque:YES];
[navigationBar addSubview:navBorder];
[navBorder release];
```
more discussion can be found [here](http://stackoverflow.com/questions/19226965/how-to-hide-ios7-uinavigationbar-1px-bottom-line)


### how to make tableview Header not show captalized letter?

```objective-c
- (void)tableView:(UITableView *)tableView willDisplayHeaderView:(UIView *)view forSection:(NSInteger)section
{
    if([view isKindOfClass:[UITableViewHeaderFooterView class]]){
        UITableViewHeaderFooterView *tableViewHeaderFooterView = (UITableViewHeaderFooterView *) view;
        
        NSString *tempStr = [tableViewHeaderFooterView.textLabel.text lowercaseString];
        tempStr = [tempStr stringByReplacingCharactersInRange:NSMakeRange(0,1) withString:[[tempStr substringToIndex:1] uppercaseString]];
        NSLog(@"temp Str is %@", tempStr);
        tableViewHeaderFooterView.textLabel.text = tempStr;
    }
}
```

### how to remove all annotations in mapview?
```objective-c
[mapView removeAnnotations:mapView.annotations]
```

### mapview examples?
[apple developer map search](https://developer.apple.com/library/ios/samplecode/MapSearch/Introduction/Intro.html)


### how to set starting view controller conditionally?
1. uncheck is initial view in storyboard
2. 
```objective-c
self.window = [[UIWindow alloc] initWithFrame:UIScreen.mainScreen.bounds];
    UIStoryboard *storyboard = [UIStoryboard storyboardWithName:@"Main" bundle:nil];
    CBFBViewController * startViewController = (CBFBViewController*)[storyboard instantiateViewControllerWithIdentifier: @"CBFBViewController"];
    
    self.window.rootViewController = startViewController;
    [self.window makeKeyAndVisible];
```
[reference](http://stackoverflow.com/questions/10428629/programatically-set-the-initial-view-controller-using-storyboards)


### whose view is not in the window hierarchy problem
normally add the present controller in viewdidappear instead of viewdidload


### how to load images asynchronously from NSURL?
```objective-c
NSURL *imageURL = [NSURL URLWithString:@"http://best-posts.com/wp-content/uploads/2014/07/hottest_world_cup_girls_07.jpg"];
    // download the image asynchronously
    NSMutableURLRequest *request = [NSMutableURLRequest requestWithURL:imageURL];
    [NSURLConnection sendAsynchronousRequest:request
                                       queue:[NSOperationQueue mainQueue]
                           completionHandler:^(NSURLResponse *response, NSData *data, NSError *error) {
                               if ( !error )
                               {
                                   
                                   UIImage *image = [[UIImage alloc] initWithData:data];
                                   [cell.profileImage setImage:image];
                               } else {
                                   NSLog(@"%@", error);
                               }
                           }];
```

### how to cache images?
currently I am using [SDWebImage](https://github.com/rs/SDWebImage)

### how to add load more function at bottom of tableview?
1. define a cell identifier as the bottom loading bar
```objective-c
-(void) tableView:(UITableView *)tableView willDisplayCell:(UITableViewCell *)cell forRowAtIndexPath:(NSIndexPath *)indexPath
{
    int lastRow=[tableArray count];
    if([indexPath row] == lastRow)
    {
        NSLog(@"going to load more");//implement your load more function
        [self.tableView reloadData];
        [self.tableView setNeedsDisplay];
        }
}
```
### tableview cell can not select
common reasons: <br>
1. do you have tap gesture in the view controller? <br>
2. did you write did selection method correctly? <br>

### how to redirect to different views based on received notifications?
http://stackoverflow.com/questions/13028233/ios-push-notification-redirect-to-view-when-app-becomes-active

### how to set uitableviewcell selection style
```objective-c
cell.selectionStyle = UITableViewCellSelectionStyleNone;
```


### iOS how to manually cache an image with sdwebimage?
[reference](http://stackoverflow.com/questions/14902835/sdwebimage-download-image-and-store-to-cache-for-key)

### iOS how to add underline to text in UIlabel
```objective-c
NSDictionary *underlineAttribute = @{NSUnderlineStyleAttributeName: @(NSUnderlineStyleSingle)};
myLabel.attributedText = [[NSAttributedString alloc] initWithString:@"Test string" 
                                                         attributes:underlineAttribute];
```
[ref](http://stackoverflow.com/questions/2711297/underline-text-in-uilabel)

### how to open address with ios map?
```objective-c
-(void)actionSheet:(UIActionSheet *)actionSheet clickedButtonAtIndex:(NSInteger)buttonIndex{
    
    NSString *btnTitle = [actionSheet buttonTitleAtIndex:buttonIndex];
    if (buttonIndex == 0) {
        if (!ISIOS6) {//ios6 调用goole网页地图
            NSString *urlString = [[NSString alloc]
                                   initWithFormat:@"http://maps.google.com/maps?saddr=&daddr=%.8f,%.8f&dirfl=d",self.naviCoordsGd.latitude,self.naviCoordsGd.longitude];
            
            NSURL *aURL = [NSURL URLWithString:urlString];
            [[UIApplication sharedApplication] openURL:aURL];
        }else{//ios7 跳转apple map
            CLLocationCoordinate2D to;
            
            to.latitude = naviCoordsGd.latitude;
            to.longitude = naviCoordsGd.longitude;
            MKMapItem *currentLocation = [MKMapItem mapItemForCurrentLocation];
            MKMapItem *toLocation = [[MKMapItem alloc] initWithPlacemark:[[MKPlacemark alloc] initWithCoordinate:to addressDictionary:nil]];
            
            toLocation.name = addressStr;
            [MKMapItem openMapsWithItems:[NSArray arrayWithObjects:currentLocation, toLocation, nil] launchOptions:[NSDictionary dictionaryWithObjects:[NSArray arrayWithObjects:MKLaunchOptionsDirectionsModeDriving, [NSNumber numberWithBool:YES], nil] forKeys:[NSArray arrayWithObjects:MKLaunchOptionsDirectionsModeKey, MKLaunchOptionsShowsTrafficKey, nil]]];
        }
    }
    if ([btnTitle isEqualToString:@"google地图"]) {
        NSString *urlStr = [NSString stringWithFormat:@"comgooglemaps://?saddr=%.8f,%.8f&daddr=%.8f,%.8f&directionsmode=transit",self.nowCoords.latitude,self.nowCoords.longitude,self.naviCoordsGd.latitude,self.naviCoordsGd.longitude];
        [[UIApplication sharedApplication] openURL:[NSURL URLWithString:urlStr]];
    }else if ([btnTitle isEqualToString:@"高德地图"]){
        NSURL *url = [NSURL URLWithString:[NSString stringWithFormat:@"iosamap://navi?sourceApplication=broker&backScheme=openbroker2&poiname=%@&poiid=BGVIS&lat=%.8f&lon=%.8f&dev=1&style=2",self.addressStr,self.naviCoordsGd.latitude,self.naviCoordsGd.longitude]];
        [[UIApplication sharedApplication] openURL:url];
        
    }else if ([btnTitle isEqualToString:@"百度地图"]){
        double bdNowLat,bdNowLon;
        bd_encrypt(self.nowCoords.latitude, self.nowCoords.longitude, &bdNowLat, &bdNowLon);

        NSString *stringURL = [NSString stringWithFormat:@"baidumap://map/direction?origin=%.8f,%.8f&destination=%.8f,%.8f&&mode=driving",bdNowLat,bdNowLon,self.naviCoordsBd.latitude,self.naviCoordsBd.longitude];
        NSURL *url = [NSURL URLWithString:stringURL];
        [[UIApplication sharedApplication] openURL:url];
    }else if ([btnTitle isEqualToString:@"显示路线"]){
        [self drawRout];
    }
}
```

Or using the URL reference

### how to add alertview with textfield
```objective-c
UIAlertView *alert = [[UIAlertView alloc] initWithTitle:@"Title"
                                                message:@"Message"
                                               delegate:self
                                      cancelButtonTitle:@"Done"
                                      otherButtonTitles:nil];
alert.alertViewStyle = UIAlertViewStylePlainTextInput;
[alert show];


-(void)alertView:(UIAlertView *)alertView clickedButtonAtIndex:(NSInteger)buttonIndex{
    NSLog(@"%@", [alertView textFieldAtIndex:0].text);
}
```

### tab bar click how to go to first view of navigation controller
```objective-c
- (void)tabBarController:(UITabBarController *)tabBarController didSelectViewController:(UIViewController *)viewController {
  if (viewController != tabBarItemForNavControllerTab) {
    [self.navControllerInFirstTab popToRootViewControllerAnimated:NO];
  }
}
```

### how to display acitivy indicator when loading image
[reference](http://stackoverflow.com/questions/11262204/show-activity-indicator-in-sdwebimage)
