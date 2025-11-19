from rest_framework import permissions

class IsParticipantOfConversation(permissions.BasePermission):
    
    def has_object_permission(self, request, view, obj):
        if request.user and request.user.is_authenticated:
            return True

        # Allow the user to access, update, and delete their own user object
        if request.user and request.user.is_authenticated:
            if obj == request.user:
                return True
            # If obj has a user attribute (e.g., Reservation), check ownership
            if hasattr(obj, 'user') and obj.user == request.user:
                return True
        return False