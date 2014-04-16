## cocoa notes

### how to link class with *.xib components?
create NSObject class, add object to file's owner, set the object to the class just created.

### NSView implement drag and drop, image seems not trigger dragenter, why? 
use 
```objective-c
[self registerForDraggedTypes:[NSArray arrayWithObjects: 
                       NSFilenamesPboardType, nil]];
```
instead of 
```objective-c
[self registerForDraggedTypes: 
                      [NSImage imagePasteboardTypes]]; 
```
### add registerForDraggedTypes one by one?
```objective-c
[self registerForDraggedTypes:[NSArray arrayWithObjects:NSPasteboardTypeString,
                                       NSPasteboardTypePDF,
                                       NSPasteboardTypeTIFF,
                                       NSPasteboardTypePNG,
                                       NSPasteboardTypeRTF,
                                       NSPasteboardTypeRTFD,
                                       NSPasteboardTypeHTML,
                                       NSPasteboardTypeTabularText,
                                       NSPasteboardTypeFont,
                                       NSPasteboardTypeRuler,
                                       NSPasteboardTypeColor,
                                       NSPasteboardTypeSound,
                                       NSPasteboardTypeMultipleTextSelection,
                                       NSPasteboardTypeFindPanelSearchOptions, nil]];
```
### why autoresizing not showing up sometimes?
uncheck auto-layout of the project. 
[reference](http://stackoverflow.com/questions/9370072/xcode-4-3-not-presenting-autoresizing-panel-in-size-inspector)

### how to add custom controls, for example, a range slider? 
follow this [tutorial](http://www.raywenderlich.com/36288/how-to-make-a-custom-control)
