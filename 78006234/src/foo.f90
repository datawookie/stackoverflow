function foo(a) result(b)
!f2py intent(in) n
!f2py intent(out) a
    implicit none

    real(kind=8), intent(in)    :: a(:,:)
    complex(kind=8)             :: b(size(a,1),size(a,2))

    b = exp((0,1)*a)

end function foo
