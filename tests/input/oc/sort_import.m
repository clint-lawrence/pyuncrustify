// should be ddd, eee, fff
#import "ddd"
#import "fff"
#import "eee"

#import "ccc"
#import "aaa"
// should be just bbb
#import "bbb"

#import "sort_import.h"
#import "sort_import+internal.h"
#import "sort_import+public.h"

#import "Action+Internal.h"
#import "Action+Public.h"
#import <UIKit/UIKit.h>
#import "Action.h"

#include "Test+Internal.h"
#include "Test.h"

#import "Something_Internal.h"
#import "Something_Public.h"
#import "Something.h"

#import "AAA"
#import "BBB.h"
#include "DDD"
#import "EEE.h"
#import <KKK>
#include "CCC.h"
