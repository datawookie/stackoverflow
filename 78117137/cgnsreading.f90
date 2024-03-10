module cgnsreading
    use cgns
    implicit none

    private

    public talk_to_cgns

contains

    subroutine error_check()
        print *, 'hi I am the bane of arthropods'
    end subroutine error_check

    subroutine talk_to_cgns()
        character(100) :: errmsg
        integer :: i = 1
        integer :: nbases = 1
        integer :: ierr

        call cg_get_error_f(errmsg)
        print *, errmsg ! Should print that there is no error
        call error_check() ! Should print its guts

        call cg_nbases_f(i,nbases,ierr) ! Throws undefined reference error

    end subroutine talk_to_cgns

end module cgnsreading
