import numpy as np
from scipy.optimize import fsolve
import scipy.special as sc
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import warnings


def power(x, a, b):
    return a*np.power(x,b)

def sigmoid(x, a, b, c, d):
    return a+((b-a)/(1+np.exp(c*(x-d))))

def small_PSP(M, wl, k):

    a=-1.189427957363609
    b=-0.6736897033833409
    c=0.042883645172411874
    AAE=1.1660747731040368
    term1=a*np.power(M,b)
    term2=np.power(c*M,-1*b)
    term3=sc.gammainc(b+1,c*M)
    term4=3*k*M
    constant=1+((a*np.power(c,-1*b)*sc.gammainc(b+1,c))/c)-(3*k)
    prefactor=6.818909583*np.power(wl/532,-AAE)
    return prefactor*(constant-((term1*term2*term3)/c)+term4)


def large_PSP(M, p, wl, k):

    a1=5.67942924724362
    a2=1.0656860970956226
    a3=0.26354898
    a4=11.42108829
    b1=2.44018476
    b2=0.59295285
    b3=0.41824767
    b4=10.10648594
    AAE=1.1660747731040368

    A=sigmoid(M,a1,a2,a3,a4)
    B=sigmoid(M,b1,b2,b3,b4)
    
    term1=(A*np.power(1/p,B-1))/(B-1)
    term2=(A*np.power(1/p,2*B-1))/(1-2*B)
    term3=A/(B-1)
    term4=A/(1-2*B)
    constant=small_PSP(M, wl, k)
    prefactor=6.818909583*np.power(wl/532,-AAE)
    return prefactor*(term1+term2-term3-term4)+constant


def meff_solver(phi):
    target=phi*((np.power(complex(1.95,0.79),2)-1)/(np.power(complex(1.95,0.79),2)+2))
    def meff(x):
        return [np.real(((np.power(complex(x[0],x[1]),2)-1)/(np.power(complex(x[0],x[1]),2)+2)))-np.real(target),
                np.imag(((np.power(complex(x[0],x[1]),2)-1)/(np.power(complex(x[0],x[1]),2)+2)))-np.imag(target)]
    sol=fsolve(meff, [1.0,0])
    return sol


def rho_solver(M,absorption,wl,k):

    def rho(p):
        a1=5.67942924724362
        a2=1.0656860970956226
        a3=0.26354898
        a4=11.42108829
        b1=2.44018476
        b2=0.59295285
        b3=0.41824767
        b4=10.10648594
        AAE=1.1660747731040368

        A=sigmoid(M,a1,a2,a3,a4)
        B=sigmoid(M,b1,b2,b3,b4)
    
        term1=(A*np.power(1/p,B-1))/(B-1)
        term2=(A*np.power(1/p,2*B-1))/(1-2*B)
        term3=A/(B-1)
        term4=A/(1-2*B)
        constant=small_PSP(M,wl,k)
        prefactor=6.818909583*np.power(wl/532,-AAE)

        return prefactor*(term1+term2-term3-term4)+constant-absorption

    sol=fsolve(rho, [1.5])
    return sol

def abs2shape_SP(diameter, coating, absorption, wavelength, k_coat=0.0, abs_error=0.0, mode='MtotMbc', r_monomer=20, asDict=True, ReturnPlot=True, PlotPoint=True):
    

    if (mode=='MtotMbc'):
        coating=coating
    elif (mode=='OC:BC' or mode=='Rbc'):
        coating=coating+1
    elif (mode=='percent_BC'):
        coating=1/(coating/100)
    else:
        warnings.warn("Error: Coating format not recognized. Coating amount can be input as 'MtotMbc', 'OC:BC', 'Rbc', or 'percent_BC'. See documentation for details.")
        return

    if (r_monomer>25 or r_monomer<15):
        warnings.warn("Error: Monomer radius must be between 15 and 25 nm.")
        return

    if (str(type(coating))=="<class 'int'>" or str(type(coating))=="<class 'float'>" or str(type(coating))=="<class 'numpy.float64'>"):
        coating=np.array([coating])
    if (str(type(absorption))=="<class 'int'>" or str(type(absorption))=="<class 'float'>" or str(type(absorption))=="<class 'numpy.float64'>"):
        absorption=np.array([absorption])
    if (str(type(diameter))=="<class 'int'>" or str(type(diameter))=="<class 'float'>" or str(type(diameter))=="<class 'numpy.float64'>"):
        diameter=np.array([diameter])
    if (str(type(abs_error))=="<class 'int'>" or str(type(abs_error))=="<class 'float'>" or str(type(abs_error))=="<class 'numpy.float64'>"):
        abs_error_val=abs_error
        abs_error=np.zeros(len(coating))
        abs_error[:]=abs_error_val
        

    if (len(coating)!=len(absorption) or len(coating)!=len(diameter) or len(absorption)!=len(diameter) or len(abs_error)!=len(coating) or len(abs_error)!=len(absorption) or len(abs_error)!=len(diameter)):
        warnings.warn("Error: Dimensions of coating, absorption, abs_error, and diameter are incompatible.")
        return

    if (len(coating)>1 or len(absorption)>1 or len(diameter)>1 or len(abs_error)>1):
        warnings.warn("Error: Only one particle at a time.")
        return


    tolerance=5 #%
    p_min=np.zeros(len(coating))
    p_avg=np.zeros(len(coating))
    p_max=np.zeros(len(coating))
    part_mass=np.zeros(len(coating))

    if (wavelength<500):
        color='purple'
    elif (wavelength>=500 and wavelength<600):
        color='green'
    elif (wavelength>=600 and wavelength<700):
        color='gold'
    elif (wavelength>=700 and wavelength<800):
        color='darkorange'
    else:
        color='red'
        
    if (PlotPoint==True or ReturnPlot==True):
        fig, (ax1) = plt.subplots(1,1,figsize=[1.3*6.4,1.3*4.8],sharex=False,constrained_layout=True)

        for axis in ['top','bottom','left','right']:
            ax1.spines[axis].set_linewidth(1.5)
            ax1.tick_params(which="minor", axis="both", direction="out", length=5, width=1.5, color="black")
            ax1.tick_params(which="major", axis="both", direction="out", length=7, width=1.5, color="black")
            ax1.tick_params(which="major",labelsize=16)
            ax1.tick_params(which="minor",labelsize=13)

    for i in range(0,len(coating)):

        r=0.5*diameter[i]*1E-7 #cm
        part_mass[i]=1E15*1.8*(4/3)*np.pi*np.power(r,3) #fg
        small_mac=small_PSP(coating[i],wavelength,k_coat)
        case1=False
        case2=False
        case3=False
        case4=False
        if (absorption[i]+abs_error[i]>=(1-(tolerance/100))*small_mac and absorption[i]>=(1-(tolerance/100))*small_mac and absorption[i]-abs_error[i]>=(1-(tolerance/100))*small_mac):
            case1=True
        elif (absorption[i]+abs_error[i]>=(1-(tolerance/100))*small_mac and absorption[i]>=(1-(tolerance/100))*small_mac):
            case2=True
        elif (absorption[i]+abs_error[i]>=(1-(tolerance/100))*small_mac):
            case3=True
        else:
            case4==True
    

        if (case1==True):
            p_min[i]=0
            p_max[i]=1
            p_avg[i]=0.5
        elif (case2==True):
            p_min[i]=0
            p_avg[i]=0.5
            sol=rho_solver(coating[i],absorption[i]-abs_error[i],wavelength,k_coat)
            p_max[i]=sol[0]
        elif (case3==True):
            p_min[i]=0
            sol=rho_solver(coating[i],absorption[i],wavelength,k_coat)
            p_avg[i]=sol[0]
            sol=rho_solver(coating[i],absorption[i]-abs_error[i],wavelength,k_coat)
            p_max[i]=sol[0]            
        else:
            sol=rho_solver(coating[i],absorption[i],wavelength,k_coat)
            p_avg[i]=sol[0]
            sol=rho_solver(coating[i],absorption[i]-abs_error[i],wavelength,k_coat)
            p_max[i]=sol[0]
            sol=rho_solver(coating[i],absorption[i]+abs_error[i],wavelength,k_coat)
            p_min[i]=sol[0]

        lower=p_avg[i]-p_min[i]
        upper=p_max[i]-p_avg[i]

        if (PlotPoint==True):
            ax1.errorbar(part_mass[i], p_avg[i], yerr=[[lower],[upper]], markersize=7, fmt = 's', mfc=color, mec = 'k', capsize=4, ecolor = color, elinewidth=1.5, mew=1.5)

    if (ReturnPlot==True or PlotPoint==True):
        
        a=r_monomer #nm
        m1=1E15*1.8*(4/3)*np.pi*np.power(a*1E-7,3) #fg
        mass=np.logspace(-2,3,200)
        rho_dlca=np.zeros(len(mass))
        rho_perc=np.zeros(len(mass))
        rho_scl=np.zeros(len(mass))

        
        for i in range(0,len(mass)):
            N=mass[i]/m1
            kf=1.2
            Df=1.78
            Rg=a*np.power(N/kf,1/Df)
            phi=kf*np.power((Df+2)/Df,-3/2)*np.power(a/Rg,3-Df)
            sol=meff_solver(phi)
            meff=complex(sol[0],sol[1])
            rho_dlca[i]=2*((2*np.pi*Rg/wavelength))*abs(meff-1)

            Df=2.5
            Rg=a*np.power(N/kf,1/Df)
            phi=kf*np.power((Df+2)/Df,-3/2)*np.power(a/Rg,3-Df)
            sol=meff_solver(phi)
            meff=complex(sol[0],sol[1])
            rho_perc[i]=2*((2*np.pi*Rg/wavelength))*abs(meff-1)

            Df=3
            Rg=a*np.power(N/kf,1/Df)
            phi=kf*np.power((Df+2)/Df,-3/2)*np.power(a/Rg,3-Df)
            sol=meff_solver(phi)
            meff=complex(sol[0],sol[1])
            rho_scl[i]=2*((2*np.pi*Rg/wavelength))*abs(meff-1)

        dlca_pars, cov = curve_fit(f=power, xdata=mass[64:71], ydata=rho_dlca[64:71], p0=[0,0], bounds=(-np.inf, np.inf))
        x1=mass[64]
        x2=mass[70]
        y1=power(x1, *dlca_pars)
        y2=power(x2, *dlca_pars)
        slope=np.log10(y2/y1)/np.log10(x2/x1)
        dlca_degrees=np.arctan(slope)*(180/np.pi)

        perc_pars, cov = curve_fit(f=power, xdata=mass[80:100], ydata=rho_perc[80:100], p0=[0,0], bounds=(-np.inf, np.inf))
        x1=mass[80]
        x2=mass[100]
        y1=power(x1, *perc_pars)
        y2=power(x2, *perc_pars)
        slope=np.log10(y2/y1)/np.log10(x2/x1)
        perc_degrees=np.arctan(slope)*(180/np.pi)

        scl_pars, cov = curve_fit(f=power, xdata=mass[100:120], ydata=rho_scl[100:120], p0=[0,0], bounds=(-np.inf, np.inf))
        x1=mass[100]
        x2=mass[120]
        y1=power(x1, *scl_pars)
        y2=power(x2, *scl_pars)
        slope=np.log10(y2/y1)/np.log10(x2/x1)
        scl_degrees=np.arctan(slope)*(180/np.pi)


        length=5
        ax1.plot(mass[:67-length],rho_dlca[:67-length],'-k',linewidth=1.5)
        ax1.plot(mass[67+length+1:],rho_dlca[67+length+1:],'-k',linewidth=1.5)
        t1=ax1.text(mass[67],power(mass[67],*dlca_pars),'fresh',ha='center',va='center',backgroundcolor='w',rotation=dlca_degrees,fontsize=9)
        t1.set_bbox(dict(facecolor='w', alpha=0, edgecolor='none'))

        length=14
        ax1.plot(mass[:90-length],rho_perc[:90-length],'-k',linewidth=1.5)
        ax1.plot(mass[90+length+1:],rho_perc[90+length+1:],'-k',linewidth=1.5)
        t2=ax1.text(mass[90],power(mass[90],*perc_pars),'partially collapsed',ha='center',va='center',backgroundcolor='w',rotation=1.55*perc_degrees,fontsize=9)
        t2.set_bbox(dict(facecolor='w', alpha=0, edgecolor='none'))

        length=10
        ax1.plot(mass[:110-length],rho_scl[:110-length],'-k',linewidth=1.5)
        ax1.plot(mass[110+length+1:],rho_scl[110+length+1:],'-k',linewidth=1.5)
        t3=ax1.text(mass[110],power(mass[110],*scl_pars),'fully collapsed',ha='center',va='center',backgroundcolor='w',rotation=1.55*scl_degrees,fontsize=9)
        t3.set_bbox(dict(facecolor='w', alpha=0, edgecolor='none'))
        
        ax1.set_xlim(0.1,1000)
        ax1.set_ylim(0.04,4)
        ax1.set_xscale('log')
        ax1.set_yscale('log')

        ax1.set_ylabel(r'$\rho_{BC}$',fontsize=18)
        ax1.set_xlabel('\n'+'BC Mass (fg)',fontsize=18)

    if (PlotPoint==True):
        plt.show()

    if (ReturnPlot==True):
        if (asDict==True):
            return fig, ax1, dict(mass=part_mass[0],rho_lower=p_min[0],rho=p_avg[0],rho_upper=p_max[0])
        else:
            return fig, ax1, part_mass[0], p_min[0], p_avg[0], p_max[0]
    else:
        if (asDict==True):
            return dict(mass=part_mass[0],rho_lower=p_min[0],rho=p_avg[0],rho_upper=p_max[0])
        else:
            return part_mass[0], p_min[0], p_avg[0], p_max[0]


def abs2shape_SD(dpg, sigma_g, coating, absorption, wavelength, k_coat=0.0, abs_error=0.0, mode='MtotMbc', r_monomer=20, asDict=True, ReturnPlot=True):
    
    if (mode=='MtotMbc'):
        coating=coating
    elif (mode=='OC:BC' or mode=='Rbc'):
        coating=coating+1
    elif (mode=='percent_BC'):
        coating=1/(coating/100)
    else:
        warnings.warn("Error: Coating format not recognized. Coating amount can be input as 'MtotMbc', 'OC:BC', 'Rbc', or 'percent_BC'. See documentation for details.")
        return

    if (sigma_g<=1):
        warnings.warn("Error: Invalid geometric standard deviation. Please Try again.")
        return

    if (r_monomer>25 or r_monomer<15):
        warnings.warn("Error: Monomer radius must be between 15 and 25 nm.")
        return

    if (str(type(coating))=="<class 'int'>" or str(type(coating))=="<class 'float'>" or str(type(coating))=="<class 'numpy.float64'>"):
        coating=np.array([coating])
    if (str(type(absorption))=="<class 'int'>" or str(type(absorption))=="<class 'float'>" or str(type(absorption))=="<class 'numpy.float64'>"):
        absorption=np.array([absorption])
    if (str(type(abs_error))=="<class 'int'>" or str(type(abs_error))=="<class 'float'>" or str(type(abs_error))=="<class 'numpy.float64'>"):
        abs_error_val=abs_error
        abs_error=np.zeros(len(coating))
        abs_error[:]=abs_error_val

    if (len(coating)!=len(absorption) or len(abs_error)!=len(coating) or len(abs_error)!=len(absorption)):
        warnings.warn("Error: Dimensions of coating, absorption, abs_error, and dp are incompatible.")
        return
    
    if (len(coating)>1 or len(absorption)>1 or len(abs_error)>1):
        warnings.warn("Error: Inputs must not be arrays.")
        return


    tolerance=5 #%
    min_d=np.exp(np.log(dpg)-np.log(sigma_g)) #nm
    max_d=np.exp(np.log(dpg)+np.log(sigma_g)) #nm
    avg_d=np.exp(np.log(dpg)) #nm
    min_r=0.5*min_d*1E-7 #cm
    max_r=0.5*max_d*1E-7 #cm
    avg_r=0.5*avg_d*1E-7 #cm
    min_mass=1E15*1.8*(4/3)*np.pi*np.power(min_r,3) #fg
    max_mass=1E15*1.8*(4/3)*np.pi*np.power(max_r,3) #fg
    avg_mass=1E15*1.8*(4/3)*np.pi*np.power(avg_r,3) #fg

    p_min=np.zeros(len(coating))
    p_avg=np.zeros(len(coating))
    p_max=np.zeros(len(coating))

    for i in range(0,len(coating)):
        
        small_mac=small_PSP(coating[i],wavelength,k_coat)
        case1=False
        case2=False
        case3=False
        case4=False
        if (absorption[i]+abs_error[i]>=(1-(tolerance/100))*small_mac and absorption[i]>=(1-(tolerance/100))*small_mac and absorption[i]-abs_error[i]>=(1-(tolerance/100))*small_mac):
            case1=True
        elif (absorption[i]+abs_error[i]>=(1-(tolerance/100))*small_mac and absorption[i]>=(1-(tolerance/100))*small_mac):
            case2=True
        elif (absorption[i]+abs_error[i]>=(1-(tolerance/100))*small_mac):
            case3=True
        else:
            case4==True
    

        if (case1==True):
            p_min[i]=1E-5
            p_max[i]=1
            p_avg[i]=np.nan
        elif (case2==True):
            p_min[i]=1E-5
            p_avg[i]=np.nan
            sol=rho_solver(coating[i],absorption[i]-abs_error[i],wavelength,k_coat)
            p_max[i]=sol[0]
        elif (case3==True):
            p_min[i]=1E-5
            sol=rho_solver(coating[i],absorption[i],wavelength,k_coat)
            p_avg[i]=sol[0]
            sol=rho_solver(coating[i],absorption[i]-abs_error[i],wavelength,k_coat)
            p_max[i]=sol[0]
        else:
            sol=rho_solver(coating[i],absorption[i],wavelength,k_coat)
            p_avg[i]=sol[0]
            sol=rho_solver(coating[i],absorption[i]-abs_error[i],wavelength,k_coat)
            p_max[i]=sol[0]
            sol=rho_solver(coating[i],absorption[i]+abs_error[i],wavelength,k_coat)
            p_min[i]=sol[0]

    
    a=r_monomer #nm
    m1=1E15*1.8*(4/3)*np.pi*np.power(a*1E-7,3) #fg
    mass=np.logspace(-2,3,200)
    rho_dlca=np.zeros(len(mass))
    rho_perc=np.zeros(len(mass))
    rho_scl=np.zeros(len(mass))
    
    for i in range(0,len(mass)):
        
        N=mass[i]/m1
        kf=1.2
        Df=1.78
        Rg=a*np.power(N/kf,1/Df)
        phi=kf*np.power((Df+2)/Df,-3/2)*np.power(a/Rg,3-Df)
        sol=meff_solver(phi)
        meff=complex(sol[0],sol[1])
        rho_dlca[i]=2*((2*np.pi*Rg/wavelength))*abs(meff-1)

        Df=2.5
        Rg=a*np.power(N/kf,1/Df)
        phi=kf*np.power((Df+2)/Df,-3/2)*np.power(a/Rg,3-Df)
        sol=meff_solver(phi)
        meff=complex(sol[0],sol[1])
        rho_perc[i]=2*((2*np.pi*Rg/wavelength))*abs(meff-1)

        Df=3
        Rg=a*np.power(N/kf,1/Df)
        phi=kf*np.power((Df+2)/Df,-3/2)*np.power(a/Rg,3-Df)
        sol=meff_solver(phi)
        meff=complex(sol[0],sol[1])
        rho_scl[i]=2*((2*np.pi*Rg/wavelength))*abs(meff-1)

    dlca_pars, cov = curve_fit(f=power, xdata=mass[64:71], ydata=rho_dlca[64:71], p0=[0,0], bounds=(-np.inf, np.inf))
    x1=mass[64]
    x2=mass[70]
    y1=power(x1, *dlca_pars)
    y2=power(x2, *dlca_pars)
    slope=np.log10(y2/y1)/np.log10(x2/x1)
    dlca_degrees=np.arctan(slope)*(180/np.pi)

    perc_pars, cov = curve_fit(f=power, xdata=mass[80:100], ydata=rho_perc[80:100], p0=[0,0], bounds=(-np.inf, np.inf))
    x1=mass[80]
    x2=mass[100]
    y1=power(x1, *perc_pars)
    y2=power(x2, *perc_pars)
    slope=np.log10(y2/y1)/np.log10(x2/x1)
    perc_degrees=np.arctan(slope)*(180/np.pi)

    scl_pars, cov = curve_fit(f=power, xdata=mass[100:120], ydata=rho_scl[100:120], p0=[0,0], bounds=(-np.inf, np.inf))
    x1=mass[100]
    x2=mass[120]
    y1=power(x1, *scl_pars)
    y2=power(x2, *scl_pars)
    slope=np.log10(y2/y1)/np.log10(x2/x1)
    scl_degrees=np.arctan(slope)*(180/np.pi)

    if (wavelength<500):
        color='purple'
    elif (wavelength>=500 and wavelength<600):
        color='green'
    elif (wavelength>=600 and wavelength<700):
        color='gold'
    elif (wavelength>=700 and wavelength<800):
        color='darkorange'
    else:
        color='red'


    if (ReturnPlot==True):
        
        fig, (ax1) = plt.subplots(1,1,figsize=[1.3*6.4,1.3*4.8],sharex=False,constrained_layout=True)

        for axis in ['top','bottom','left','right']:
            ax1.spines[axis].set_linewidth(1.5)

        ax1.tick_params(which="minor", axis="both", direction="out", length=5, width=1.5, color="black")
        ax1.tick_params(which="major", axis="both", direction="out", length=7, width=1.5, color="black")
        ax1.tick_params(which="major",labelsize=16)
        ax1.tick_params(which="minor",labelsize=13)

        length=5
        ax1.plot(mass[:67-length],rho_dlca[:67-length],'-k',linewidth=1.5)
        ax1.plot(mass[67+length+1:],rho_dlca[67+length+1:],'-k',linewidth=1.5)
        t1=ax1.text(mass[67],power(mass[67],*dlca_pars),'fresh',ha='center',va='center',backgroundcolor='w',rotation=dlca_degrees,fontsize=9)
        t1.set_bbox(dict(facecolor='w', alpha=0, edgecolor='none'))

        length=14
        ax1.plot(mass[:90-length],rho_perc[:90-length],'-k',linewidth=1.5)
        ax1.plot(mass[90+length+1:],rho_perc[90+length+1:],'-k',linewidth=1.5)
        t2=ax1.text(mass[90],power(mass[90],*perc_pars),'partially collapsed',ha='center',va='center',backgroundcolor='w',rotation=1.55*perc_degrees,fontsize=9)
        t2.set_bbox(dict(facecolor='w', alpha=0, edgecolor='none'))

        length=10
        ax1.plot(mass[:110-length],rho_scl[:110-length],'-k',linewidth=1.5)
        ax1.plot(mass[110+length+1:],rho_scl[110+length+1:],'-k',linewidth=1.5)
        t3=ax1.text(mass[110],power(mass[110],*scl_pars),'fully collapsed',ha='center',va='center',backgroundcolor='w',rotation=1.55*scl_degrees,fontsize=9)
        t3.set_bbox(dict(facecolor='w', alpha=0, edgecolor='none'))

        ax1.plot(avg_mass,np.mean(p_avg),'s',color=color,mec='k',markersize=10)
        
        ax1.set_xlim(0.1,1000)
        ax1.set_ylim(0.04,4)
        ax1.set_xscale('log')
        ax1.set_yscale('log')

        if (case1==True or case2==True or case3==True):
            N=min_mass/m1
            kf=1.2
            Df=1.78
            Rg=a*np.power(N/kf,1/Df)
            phi=kf*np.power((Df+2)/Df,-3/2)*np.power(a/Rg,3-Df)
            sol=meff_solver(phi)
            meff=complex(sol[0],sol[1])
            p_min1=2*((2*np.pi*Rg/wavelength))*abs(meff-1)

            N=max_mass/m1
            Rg=a*np.power(N/kf,1/Df)
            phi=kf*np.power((Df+2)/Df,-3/2)*np.power(a/Rg,3-Df)
            sol=meff_solver(phi)
            meff=complex(sol[0],sol[1])
            p_min2=2*((2*np.pi*Rg/wavelength))*abs(meff-1)
            x=np.array([min_mass,max_mass])
            y1=np.array([p_min1,p_min2])
            y2=np.array([np.max(p_max),np.max(p_max)])
            ax1.fill_between(x,y1,y2,facecolor=color,alpha=0.4)
            
        else:
            ax1.add_patch(Rectangle((min_mass, np.min(p_min)),max_mass-min_mass, np.max(p_max)-np.min(p_min),fc =color, alpha=0.4, ec =color,lw = 1.5))

        ax1.set_ylabel(r'$\rho_{BC}$',fontsize=18)
        ax1.set_xlabel('\n'+'BC Mass (fg)',fontsize=18)

    if (ReturnPlot==True):
        if (asDict==True):
            return fig, ax1, dict(min_mass=min_mass,avg_mass=avg_mass,max_mass=max_mass,rho_lower=p_min[0],rho=p_avg[0],rho_upper=p_max[0])
        else:
            return fig, ax1, min_mass, avg_mass, max_mass, p_min[0], p_avg[0], p_max[0]
    else:
        if (asDict==True):
            return dict(lower_mass=min_mass, avg_mass=avg_mass, upper_mass=max_mass, rho_lower=p_min[0], rho=p_avg[0], rho_upper=p_max[0])
        else:
            return min_mass, avg_mass, max_mass, p_min[0], p_avg[0], p_max[0]


def shape2abs_SD(dpg, sigma_g, coating_avg, coating_stdev, collapse, wavelength, k_coat=0.00, mode='MtotMbc', r_monomer=20, DataPoints=False, ShowPlots=True):

    if (mode=='MtotMbc'):
        coating_avg=coating_avg
    elif (mode=='OC:BC' or mode=='Rbc'):
        coating_avg=coating_avg+1
    elif (mode=='percent_BC'):
        x=coating_avg
        coating_avg=1/(coating_avg/100)
        coating_stdev=(1/((x-coating_stdev)/100))-coating_avg
    else:
        warnings.warn("Error: Coating format not recognized. Coating amount can be input as 'MtotMbc', 'OC:BC', 'Rbc', or 'percent_BC'. See documentation for details.")
        return

    if (sigma_g<=1):
        warnings.warn("Error: Invalid geometric standard deviation. Please Try again.")
        return

    if (r_monomer>25 or r_monomer<15):
        warnings.warn("Error: Monomer radius must be between 15 and 25 nm.")
        return
    
    if (collapse=='fresh'):
        Df=1.78
    elif (collapse=='partial'):
        Df=2.5
    elif (collapse=='full'):
        Df=3
    else:
        warnings.warn("Error: Morphology not recognized. Input can be 'fresh', 'partial', or 'full'. See documentation for details.")
        return

    N=10000
    M=np.zeros(N)
    dp=np.zeros(N)
    MAC=np.zeros(N)
    mass=np.zeros(N)
    dp_avg=np.log(dpg)
    dp_stdev=np.log(sigma_g)
    m1=1E15*1.8*(4/3)*np.pi*np.power(r_monomer*1E-7,3) #fg
    kf=1.2

    for i in range(0,N):

        rho=5
        M[i]=0.1

        while (M[i]<1):
            M[i]=np.random.normal(coating_avg,coating_stdev)

        while (rho>4):
            
            dp[i]=np.random.lognormal(dp_avg,dp_stdev)
            r=0.5*dp[i]*1E-7 #cm
            mass[i]=1E15*1.8*(4/3)*np.pi*np.power(r,3) #fg
            N=mass[i]/m1
            Rg=r_monomer*np.power(N/kf,1/Df)
            phi=kf*np.power((Df+2)/Df,-3/2)*np.power(r_monomer/Rg,3-Df)
            sol=meff_solver(phi)
            meff=complex(sol[0],sol[1])
            rho=2*((2*np.pi*Rg/wavelength))*abs(meff-1)

        if (rho<=1):
            MAC[i]=small_PSP(M[i],wavelength,k_coat)
        elif (rho<4):
            MAC[i]=large_PSP(M[i],rho,wavelength,k_coat)

        if (mode=='MtotMbc'):
            M[i]=M[i]
        elif (mode=='OC:EC' or mode=='Rbc'):
            M[i]=M[i]-1
        elif (mode=='percent_BC'):
            M[i]=(1/M[i])*100
            
    if (ShowPlots==True):
        fig1, ((ax1,ax2),(ax3,ax4)) = plt.subplots(2,2,figsize=[1.3*6.4,1.3*4.8],sharex=False,constrained_layout=True)
        bins=np.logspace(np.log10(10),np.log10(10000),100)
        ax1.hist(dp, density=True, bins=bins, alpha=0.6, color='grey', ec='grey')
        ax1.set_xlabel('Mass-Equivalent Diameter (nm)')
        ax1.set_ylabel('Probability Density \n')
        ax1.set_xlim(10,10000)
        ax1.set_xscale('log')
        ax2.hist(M, density=True, bins=100, alpha=0.6, color='grey', ec='grey')
        ax2.set_xlim(round(coating_avg-(5*coating_stdev)),round(coating_avg+(5*coating_stdev)))

        if (mode=='MtotMbc'):
            ax2.set_xlabel(r'$M_{tot}/M_{BC}$')
        elif (mode=='OC:EC'):
            ax2.set_xlabel('OC:EC')
        elif (mode=='percent_BC'):
            ax2.set_xlabel('BC Fraction (%)')
            ax2.set_xlim(0,100)
        elif (mode=='Rbc'):
            ax2.set_xlabel(r'$R_{BC}$')

            
        bins=np.logspace(np.log10(0.001),np.log10(1000),100)
        ax3.hist(mass, density=True, bins=bins, alpha=0.6, color='grey', ec='grey')
        ax3.set_xlabel('Mass (fg)')
        ax3.set_ylabel('Probability Density \n')
        ax3.set_xlim(0.001,1000)
        ax3.set_xscale('log')

        ax4.hist(MAC, density=True, bins=100, alpha=0.6, color='grey', ec='grey')
        ax4.set_xlim(round(np.mean(MAC)-(5*np.std(MAC))),round(np.mean(MAC)+(5*np.std(MAC))))
        ax4.set_xlabel(r'MAC$_{BC}$ (m$^2$/g)')
        plt.show()

    if (DataPoints==True):
        return dp, M, MAC
    else:
        return dict(dp_avg=np.mean(dp), dp_stdev=np.std(dp), coating_avg=np.mean(M), coating_stdev=np.std(M), MAC_avg=np.mean(MAC), MAC_std=np.std(MAC))
    



def shape2abs_SP(dp, coating, collapse, wavelength, k_coat=0.00, mode='MtotMbc', r_monomer=20, asDict=True):

    if (mode=='MtotMbc'):
        coating=coating
    elif (mode=='OC:BC' or mode=='Rbc'):
        coating=coating+1
    elif (mode=='percent_BC'):
        coating=1/(coating/100)
    else:
        warnings.warn("Error: Coating format not recognized. Coating amount can be input as 'MtotMbc', 'OC:BC', 'Rbc', or 'percent_BC'. See documentation for details.")
        return

    if (r_monomer>25 or r_monomer<15):
        warnings.warn("Error: Monomer radius must be between 15 and 25 nm.")
        return
    
    if (collapse=='fresh'):
        Df=1.78
    elif (collapse=='partial'):
        Df=2.5
    elif (collapse=='full'):
        Df=3
    else:
        warnings.warn("Error: Morphology not recognized. Input can be 'fresh', 'partial', or 'full'. See documentation for details.")
        return


    m1=1E15*1.8*(4/3)*np.pi*np.power(r_monomer*1E-7,3) #fg
    kf=1.2

    r=0.5*dp*1E-7 #cm
    mass=1E15*1.8*(4/3)*np.pi*np.power(r,3) #fg
    N=mass/m1
    Rg=r_monomer*np.power(N/kf,1/Df)
    phi=kf*np.power((Df+2)/Df,-3/2)*np.power(r_monomer/Rg,3-Df)
    sol=meff_solver(phi)
    meff=complex(sol[0],sol[1])
    rho=2*((2*np.pi*Rg/wavelength))*abs(meff-1)

    if (rho<=1):
        MAC=small_PSP(coating,wavelength,k_coat)
    elif (rho<4):
        MAC=large_PSP(coating,rho,wavelength,k_coat)
    else:
        warnings.warn("Error: Phase shift parameter is > 4, outside the fitting range of this package.")
        return

    if (mode=='MtotMbc'):
        coating=coating
    elif (mode=='OC:EC' or mode=='Rbc'):
        coating=coating-1
    elif (mode=='percent_BC'):
        coating=(1/coating)*100
        

    if (asDict==True):
        return dict(dp=dp,coating=coating, MAC=MAC)
    else:
        return dp, coating, MAC


    
