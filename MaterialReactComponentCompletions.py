import sublime_plugin
import sublime

rc_attribute = ["absolute","action","actionPosition","active","activeStep","align","alignContent","alignItems","alt","alternativeLabel","anchorOrigin","anchorPosition","anchorReference","autoComplete","autoFocus","autoHideDuration","avatar","button","buttonRef","cellHeight","centered","centerRipple","checked","checkedIcon","classes","className","clickable","closeAfterTransition","collapsedHeight","color","cols","completed","component","container","defaultExpanded","defaultValue","delay","deleteIcon","dense","direction","disableAnimation","disableAutoFocusItem","disableBackdropClick","disableBackdropTransition","disabled","disableDiscovery","disableEnforceFocus","disableEscapeKeyDown","disableFocusListener","disableFocusRipple","disableGutters","disableHoverListener","disableListWrap","disablePadding","disablePointerEvents","disablePortal","disableRestoreFocus","disableRipple","disableShrink","disableSpacing","disableSticky","disableSwipeToOpen","disableTouchListener","disableTouchRipple","disableTypography","disableUnderline","disableWindowBlurListener","display","displayEmpty","divider","dividers","edge","elevation","endAdornment","enterDelay","enterTouchDelay","error","exclusive","expanded","filled","fixed","focused","focusRipple","focusVisibleClassName","fontSize","fullScreen","fullWidth","gutterBottom","hidden","hideBackdrop","hideSortIcon","hover","href","htmlColor","hysteresis","icon","id","image","imgProps","implementation","in","indeterminate","indeterminateIcon","indicatorColor","initialWidth","inputProps","inputRef","inset","interactive","invisible","item","itemsAfterCollapse","itemsBeforeCollapse","justify","keepMounted","label","labelPlacement","labelWidth","leaveDelay","leaveTouchDelay","lg","lgDown","lgUp","light","margin","marginThreshold","max","maxItems","maxWidth","md","mdDown","mdUp","min","minFlingVelocity","ModalProps","multiline","name","native","nonLinear","notched","noWrap","onChange","onDelete","onFocusVisible","only","open","orientation","padding","PaperComponent","PaperProps","paragraph","placeholder","placement","position","raised","readOnly","required","resumeHideDuration","row","rows","rowsMax","rowsPerPageOptions","scope","scroll","scrollButtons","selected","separator","shapeRendering","showLabels","showZero","shrink","size","sizes","SlideProps","sm","smDown","smUp","sortDirection","spacing","square","src","srcSet","step","subheader","subheaderTypographyProps","swipeAreaWidth","textColor","thickness","timeout","title","titleAccess","titlePosition","titleTypographyProps","tooltipOpen","tooltipPlacement","TouchRippleProps","transformOrigin","transition","transitionDuration","TransitionProps","type","underline","value","valueBuffer","variant","variantMapping","vertical","viewBox","wrap","wrapped","xl","xlDown","xlUp","xs","xsDown","xsUp","zeroMinWidth"]
rc_value = ["absolute","action","always","anchor","anchorEl","anchorPosition","asc","auto","baseline","block","body","body1","body2","bottom","bottom-end","bottom-start","buffer","button","caption","center","column","column-reverse","contained","css","default","dense","desktop","determinate","dot","dsc","elevation","end","error","extended","false","filled","fixed","flex-end","flex-start","footer","fullWidth","h1","h2","h3","h4","h5","h6","head","horizontal","horizontal:","hover","indeterminate","inherit","initial","inline","inset","js","justify","large","left","left-end","left-start","lg","md","medium","menu","middle","name","none","normal","nowrap","off","on","outlined","overline","permanent","persistent","primary","query","relative","reset","right","right-end","right-start","round","row","row-reverse","scrollable","selectedMenu","sm","small","space-around","space-between","space-evenly","srOnly","standard","start","static","sticky","stretch","submit","subtitle1","subtitle2","temporary","text","textPrimary","textSecondary","top","top-end","top-start","true","vertical","vertical:","wrap","wrap-reverse","xl","xs"]

class MaterialReactCompletion(sublime_plugin.EventListener):
    """
    Provide tag completions for Bootstrap elements and data-uk attributes
    """
    def __init__(self):

        self.attribute_completions = [("%s \tM-Ui" % s, s+ '="$1"\n$2') for s in rc_attribute]
        self.value_completions = [("%s \tM-Ui" % s, s) for s in rc_value]

    def on_query_completions(self, view, prefix, locations):

        if view.match_selector(locations[0], "source.js string.quoted"):
            #inside double quote
            return  self.value_completions
        elif view.match_selector(locations[0], "source.js meta.jsx.js"):
            return self.attribute_completions #inside tag but not in attribute
        else:
            return []

