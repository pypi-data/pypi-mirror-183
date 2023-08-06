## Release History

### 0.2.9

> - Completed dataclass for DataSchema to allow creation and pulling of objects
> - dataschema is now renamed to data_schema in the SDK to be consistent, 
old usages are still possible but you will receive a deprecation warning. Please use the new way of accessing data_schemas.
> - Experimental endpoint for getting workgroups
> - Fixed some issues with properties on projects
> - Fix issue with get_cohorts()
> - Fixed issue with project.aimodels returning incorrect dataclasses
> - Fixed issue with certain functions not working

### 0.2.8

> - Improved documentation for creating/running AI Models
> - Fixed the bug you reported about training where unset values in the input were being sent to the backend
> - Added ability to search by name as well as a regrouping utility function for the result of metrics
> - Added a new Python Code Generalized Compute Type
