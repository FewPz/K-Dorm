import { LogOut } from "lucide-react";
import { Button } from "./ui/button";
import { useAuthContext } from "@/contexts/AuthContext";
import { useCallback } from "react";

const StaffRightMenu = () => {
  const { logout } = useAuthContext();

  const handleLogout = useCallback(async () => {
    await logout();
  }, [logout]);
  return (
    <div className="bg-orange-100 h-full flex flex-col justify-end items-center">
      <Button
        variant="ghost"
        size="icon"
        className="rounded-full mb-4 hover:bg-orange-300"
        onClick={handleLogout}
      >
        <LogOut className="h-6 w-6" />
      </Button>
    </div>
  );
};

export default StaffRightMenu;