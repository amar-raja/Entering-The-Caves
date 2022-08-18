def coppersmith_howgrave_univariate(pol, modulus, beta, mm, tt, XX):
    
    dd = pol.degree()
    nn = dd * mm + tt

    if not 0 < beta <= 1:
        raise ValueError("beta should belong in (0, 1]")

    if not pol.is_monic():
        raise ArithmeticError("Polynomial must be monic.")
    
    polZ = pol.change_ring(ZZ)
    x = polZ.parent().gen()
    gg = []
    for ii in range(mm):
        for jj in range(dd):
            gg.append((x * XX)**jj * modulus**(mm - ii) * polZ(x * XX)**ii)
    for ii in range(tt):
        gg.append((x * XX)**ii * polZ(x * XX)**mm)

    BB = Matrix(ZZ, nn)

    for ii in range(nn):
        for jj in range(ii+1):
            BB[ii, jj] = gg[ii][jj]

    # LLL
    BB = BB.LLL()

    # transform shortest vector in polynomial
    new_pol = 0
    for ii in range(nn):
        new_pol += x**ii * BB[0, ii] / XX**ii

    # factor polynomial
    potential_roots = new_pol.roots()

    # test roots
    roots = []
    for root in potential_roots:
        if root[0].is_integer():
            result = polZ(ZZ(root[0]))
            if gcd(modulus, result) >= modulus^beta:
                roots.append(ZZ(root[0]))

    
    return roots
e = 5
N = 84364443735725034864402554533826279174703893439763343343863260342756678609216895093779263028809246505955647572176682669445270008816481771701417554768871285020442403001649254405058303439906229201909599348669565697534331652019516409514800265887388539283381053937433496994442146419682027649079704982600857517093
C = 25925046408515034418963906289645675378763632405515886311299791906159166174881760556207167987492823232877859290784269690322012941812534517163842608750437955467761604342479212924250621732363506527240247204137378081768711202012790150577857091656600996623255766642887573542884527180241094751578817965054371251780

ZmodN = Zmod(N)

def decrypt(padding):
    z=""
    for i in padding:
    	i=bin(ord(i))[2:]
    	z+='0'*(8-len(i))+i
    padding = int(z,2)
    for le in range(0, 501):         
	

        P.<x> = PolynomialRing(ZmodN)
        pol = ((padding<<le) + x)^e - C
        dd = pol.degree()
        beta = 1                                
        epsilon = beta / 7                      
        mm = ceil(beta**2 / (dd * epsilon))     
        tt = floor(dd * mm * ((1/beta) - 1))    
        XX = ceil(N**((beta**2/dd) - epsilon))  

        roots = coppersmith_howgrave_univariate(pol, N, beta, mm, tt, XX)
        if roots!=[]:
            print("length of unknown part is: ",le)
            password=bin(roots[0])[2:]
            print ("A solution has been found out. It is : "+password)
            final_password=""
            for i in range(len(password)%8,len(password),8):
                final_password+=chr(int(password[i:i+8],2))
            print("\nDecrypted password is: ",final_password)
            return

    print('There is no solution for this padding')

padding="ANV: This door has RSA encryption with exponent 5 and the password is"
decrypt(padding)